#!/usr/bin/env python3

from yattag import Doc, indent
from datetime import date
import os, re

# Any new term types must be added to this dictionary for sorting
termIDDict = { 'Spring': 'b', 'Fall': 'd', 'HoTTEST Event For Junior Researchers': 'a', 'HoTTEST Conference' : 'c', 'HoTTEST Summer School' : 'c'}
monthDict = { 'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12 }

class Talk:
    def __init__(self, term, date, speaker, school, title, ytlink, slides, abstract):
        self.term = term
        self.termID = ''
        self.date = date
        self.dateID = ''
        self.speaker = speaker
        self.school = school
        self.title = title
        self.ytlink = ytlink
        self.slides = slides
        self.abstract = abstract

# Given file name in the folder "TalkInfo", parses file into a Talk object
def readFile(fileName):
    newTalk = Talk('', '', '', '', '', '', [], '')
    with open('./TalkInfo/' + fileName, encoding='utf8') as f:
        lines = f.readlines()
        inAbstract = False
        lineNumber = 0
        for line in lines:
            line = line.strip()
            if not line: # skip whitespace-only lines
                continue
            lineNumber += 1
            if line.lower().startswith('abstract:') or inAbstract:
                if not inAbstract:
                    newTalk.abstract = '<p>' + line[9:].strip() + '</p>'
                    inAbstract = True
                else:
                    newTalk.abstract += '<p>' + line +'</p>'
            elif line.lower().startswith('term:'):
                newTalk.term = line[5:].strip()
                if newTalk.term[:-5] in termIDDict:
                    try:
                        yearNum = int(newTalk.term[-4:])
                    except ValueError:
                        raise Exception(fileName + ': Term does not end in four-digit year')
                    newTalk.termID = (yearNum, termIDDict[newTalk.term[:-5]])
                else:
                    raise Exception(fileName + ': Term type not found - new term types must be added to termIDDict for sorting')
            elif line.lower().startswith('date:'):
                newTalk.date = line[5:].strip()
                if newTalk.date[:3] in monthDict:
                    monthNum = monthDict[newTalk.date[:3]]
                    try:
                        dayNum = int(newTalk.date[-2:])
                    except ValueError:
                        dayNum = 0
                    newTalk.dateID = (monthNum, dayNum)
                else:
                    raise Exception(fileName + ': Date entry ill-formed')
            elif line.lower().startswith('speaker:'):
                newTalk.speaker = line[8:].strip()
            elif line.lower().startswith('school:'):
                newTalk.school = line[7:].strip()
            elif line.lower().startswith('title:'):
                newTalk.title = line[6:].strip()
            elif line.lower().startswith('youtube:'):
                newTalk.ytlink = line[8:].strip()
            elif line.lower().startswith('slides:'):
                newTalk.slides = line[7:].strip().split()
            else:
                raise Exception(fileName + ': Improperly formatted label in line ' + str(lineNumber) + ' - "' + line + '"')
        if newTalk.title == '':
            newTalk.title = 'TBA'
        return newTalk

# Function for testing if a talk object is missing any critical components
def validateTalk(talk):
    if talk.date.strip() == '':
        raise Exception('Talk missing date entry')
    elif talk.term.strip() == '':
        raise Exception('Talk on ' + talk.date + ' missing term entry')
    elif talk.speaker.strip() == '':
        raise Exception('Talk on ' + talk.date + ', ' + talk.term + ' missing speaker name')
    elif talk.title.strip() == '':
        raise Exception('Talk "' + talk.speaker + '-' + talk.date + '" missing talk title')
    elif talk.abstract.strip() == '':
        raise Exception('Talk "' + talk.speaker + '-' + talk.date + '" missing abstract')

# Check whether the talk is in the future
def isFuture(talk):
    today = (date.today().year, date.today().month, date.today().day)
    talkDate = (talk.termID[0], talk.dateID[0], talk.dateID[1])
    return today < talkDate

# Parse and organize talks
pastTalks = {}
futureTalks = {}
for file in os.listdir('./TalkInfo'):
    if not (file.startswith('.') or file.endswith('~')): # Ignore files with unusual names (system generated, etc.)
        thisTalk = readFile(file)
        validateTalk(thisTalk)
        if isFuture(thisTalk):
            futureTalks.setdefault(thisTalk.termID, {}).setdefault(thisTalk.dateID, []).append(thisTalk)
        else:
            pastTalks.setdefault(thisTalk.termID, {}).setdefault(thisTalk.dateID, []).append(thisTalk)

# Start creating HTML document
doc, tag, text, line = Doc().ttl()

docHead = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="utf-8">
<link rel="stylesheet" href="css/style.css">
<base target="_blank">
<title>HoTTEST</title>
<link rel="icon" type="image/x-icon" href="/images/favicon.svg">
</head>
<body>
<div id="container">

<div id="title">
    <div style="width: 300px;"></div>
    <h1 style="flex: 1;text-align: center; margin: 0;">HoTTEST</h1>
    <img src="images/universal-cover.png" alt="Universal Cover of S^1" style="width: 250px;">
</div>
<hr style="border: 1px solid #888ebe;">
<p style="margin-left: auto; margin-right: auto; text-align: center; max-width: 1000px;">
    Homotopy Type Theory Electronic Seminar Talks (HoTTEST) is a series of research talks by leading experts in Homotopy Type Theory.
    The seminar is open to all, although <strong>familiarity with Homotopy Type Theory will be assumed</strong>.
    To attend a talk, please follow the instructions below.</p>
<hr style="border: 1px solid #888ebe;">

<h2>Essential Information</h2>
<ul>
    <li><strong>Time: </strong>Alternate Thursdays at 11:30 AM Eastern (60-minute talk + 30-minute discussion).</li>
    <li><strong>Mailing list: </strong><a href="https://groups.google.com/forum/#!forum/hott-electronic-seminar-talks">HoTT Electronic Seminar Talks</a> (for updates).</li>
    <li><strong>Google calendar: </strong><a href="https://calendar.google.com/calendar/embed?src=0a4ik9o5vhkgjlnk6no3ttnuko%40group.calendar.google.com&amp;ctz=America%2FToronto">Seminar Calendar</a>.</li>
    <li><strong>YouTube channel: </strong><a href="https://www.youtube.com/channel/UC-9jDbJ-HegCFuWuam1SfvQ">HoTTEST</a>.</li>
    <li><strong>Organizers: </strong>
        <a href="https://www.carloangiuli.com/">Carlo Angiuli</a>,
        <a href="https://jdc.math.uwo.ca/">Dan Christensen</a>,
        <a href="https://www.math.uwo.ca/faculty/kapulkin/index.html">Chris Kapulkin</a>, and
        <a href="https://emilyriehl.github.io/">Emily Riehl</a>.</li>
    <li><strong>Website by: </strong><a href="https://doolster.github.io/">Zack Dooley</a></li>
</ul>

<h2>How to Attend?</h2>
<p>We are using <a href="https://zoom.us">Zoom</a> for the talks. Please install the software and make at least one test call before joining a talk. To join follow the link:</p>
<p style="text-align: center; margin: 20px;"><a href="https://zoom.us/j/994874377">https://zoom.us/j/994874377</a></p>

<div class="expand-all-container">
    <button id="expand-term-btn" class="button expand-all">Expand Terms</button>
    <button id="expand-abst-btn" class="button expand-all">Expand Abstracts</button>
</div>
"""

# Adding the static top of the page to doc (Title to "Expand All" button) (probably a better way to do this)
doc.asis(docHead)

# Loop through given talk dictionary to generate HTML
def printTalks(talkDict, reverseChronological=False):
    for termID in sorted(talkDict, reverse=reverseChronological):
        thisTerm = talkDict[termID] # Dictionary of the current term
        with tag('button', klass='accordion'):
            text(next(iter(thisTerm.values()))[0].term)
        with tag('div', klass='panel'):
            with tag('table'):
                with tag('tr'):
                    line('th', 'Date')
                    line('th', 'Speaker')
                    line('th', 'Talk Information')
                # Every date in this term
                for dateID in sorted(thisTerm, reverse=reverseChronological):
                    # Every talk on this date
                    for talk in sorted(thisTerm[dateID], key=lambda talk: talk.title):
                        with tag('tr'):
                            line('td', talk.date, klass='date')
                            with tag('td', klass='speaker'):
                                text(talk.speaker)
                                if talk.school != '':
                                    line('div', talk.school, klass='school')
                            with tag('td'):
                                with tag('p', klass='talk-title'):
                                    text(talk.title, ' ')
                                    with tag('span', klass='icons'):
                                        if talk.ytlink != '':
                                            with tag('a', href=talk.ytlink):
                                                doc.stag('img', src='images/youtube.webp', width='20', alt='YouTube video')
                                        for slide in talk.slides:
                                            with tag('a', href='hottestfiles/' + slide):
                                                doc.stag('img', src='images/pdf.png', width='20', alt='Slides')
                                with tag('div', klass='abstract'):
                                    doc.asis(talk.abstract)

printTalks(futureTalks)
doc.asis("<h2>Past Talks</h2>")
printTalks(pastTalks, True)

docFoot = """
<script src="js/control.js"></script>

</div>
</body>
</html>
"""

# Add static end to doc and write doc to file
doc.asis(docFoot)

with open('index.html', 'w', encoding='utf8') as f:
    f.write(indent(doc.getvalue()))
f.close()
