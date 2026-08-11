<h2>Overview</h2>

This repository is used to generate the HoTTEST website:  https://hottest-seminar.github.io/

<p>
The information for each talk is stored in a file in the TalkInfo folder, using a file name like AndyPitts-Sep20.txt.
See below for details about the format.

<p>
At the beginning of each term, the termGenerator.py script can be used generate these
files, with just the essential information filled in.
See also calendarGenerator.py for how to create the initial Google calendar entries
for a term.

<p>
After soliciting a title and abstract, you can update the appropriate file.

<p>
Whenever a TalkInfo file is created or changed, you need to run the
script <tt>./indexGenerator.py</tt> which updates index.html.
(This script requires the Yattag Python library.)
You can preview this in your local browser to make sure it looks correct.
Then you commit the changes to the TalkInfo file and index.html, push
your commit to github, and wait around 30 seconds.
Then reload the website https://hottest-seminar.github.io/ to check that all is good.

<p>
Aside: If you run <tt>indexGenerator.py</tt> on the day a seminar occurs, it will become a "past" talk.
If you still want it to be a future talk, you can run:
<tt>faketime yesterday ./indexGenerator.py</tt>
(after installing faketime on your system).

<p>
When you get the pdf file after a talk, you put it in the hottestfiles
folder, following the naming convention there, and update the TalkInfo file to refer to it.
Then regenerate as described above, and commit the TalkInfo file,
the pdf file, and index.html.

<p>
Dan currently handles adding the YouTube links.

<h2>Formatting for talk files</h2>

Term: TERM YYYY<br>
Date: MON DD<br>
Speaker: SPEAKER NAME<br>
School: SCHOOL/INSTITUTION<br>
Title: TALK TITLE<br>
YouTube: YOUTUBE LINK<br>
Slides: SLIDE_FILENAME_1 SLIDE_FILENAME_2 ... <br>
Abstract: ABSTRACT CONTENT<br>
ABSTRACT CONTENT<br>
...<br>

<p>
Notes:
<ul>
  <li>TERM should be either "Spring" or "Fall" for regular sessions, special terms can be added (such as the Jr. Researcher Event), but a corresponding entry must be added to termIDDict in indexGenerator.py for sorting purposes.</li>
  <li>YYYY is the year.</li>
  <li>MON should be the first three letters of the month.</li>
  <li>DD is the day, as one or two digits.</li>
  <li>SPEAKER is the name of the speaker, with first name first.</li>
  <li>SCHOOL/INSTITUTION is the name of the name of the speaker's affiliation; this can be left empty.</li>
  <li>TALK TITLE is the title of the talk, usually with only the first word and proper nouns capitalized.</li>
  <li>YOUTUBE LINK is the relevant link.</li>
  <li>SLIDE_FILENAME_X are the relevant filenames (no "hottestfiles/" prefix necessary); multiple pdfs can be attached to a single talk and should be separated by a single space.</li>
  <li>ABSTRACT CONTENT is the abstract, with each paragraph as a single long line.  A line break indicates a new paragraph, and there should be no empty lines between paragraphs. The abstract must always be the last entry.</li>
  <li>HTML can be added to ABSTRACT CONTENT and will be rendered correctly, e.g., if you want to include a hyperlink.</li>
</ul>

Things that will affect page generation (<tt>indexGenerator.py</tt> will throw an exception):
<ul>
  <li>Misspelled line starters</li>
  <li>Improperly formatted term or date entries</li>
  <li>Certain missing entries (e.g. Term, Date, Speaker)</li>
  <li>"Abstract:" not being the last entry (the exception that will show up in this case is for missing entries of whatever was below "Abstract:")</li>
  <li>&gt; and &lt; symbols in abstract (must be replaced with &amp;gt; and &amp;lt; to not get the following error: yattag.indentation.XMLTokenError) </li>
</ul>

Things that will _not_ affect page generation:
<ul>
  <li>File name</li>
  <li>Whitespace differences (either before or after lines, between entry label and content, or general blank lines)</li>
  <li>Ordering of entries (besides "Abstract:" which must go last)</li>
</ul>
