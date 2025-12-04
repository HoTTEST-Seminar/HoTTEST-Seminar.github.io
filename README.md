<h2>EXAMPLE OF CORRECT FORMATTING FOR TALK FILES</h2>

Term: TERM YYYY<br>
Date: MON DD<br>
Speaker: SPEAKER NAME<br>
School: SCHOOL/INSTITUTION
Title: TALK TITLE<br>
YouTube: YOUTUBE LINK<br>
Slides: SLIDE_FILENAME_1 SLIDE_FILENAME_2 ... <br>
Abstract: ABSTRACT CONTENT<br>
ABSTRACT CONTENT<br>
...<br>

New talk files should be added to the TalkInfo folder.
The termGenerator.py script can help with this.  See that file for instructions.

<p>
After creating/updating talk files, run <tt>./indexGenerator.py</tt>.
If you are running this on the day a seminar occurs, if will become a "past" talk.
If you still want it to be a future talk, you can run:
<tt>faketime yesterday ./indexGenerator.py</tt>
(after installing faketime on your system).

<p>
NOTES:
<ul>
  <li>TERM should be either "Spring" or "Fall" for regular sessions, special terms can be added (such as the Jr. Researcher Event), but a corresponding entry must be added to termIDDict in indexGenerator.py for sorting purposes.</li>
  <li>YYYY is the year.</li>
  <li>MON should be the shortened form of the month (Jan, Sept, etc. this is just for consistency purposes, as long as MON starts with the correct three letters it will be sorted correctly).</li>
  <li>DD is the day, if it is a single digit, make sure there is a space between MON and DD.</li>
  <li>SPEAKER is the name of the speaker</li>
  <li>SCHOOL/INSTITUTION is the name of the name of the speaker's affiliation, this is okay to leave empty.</li>
  <li>TALK TITLE is the title of the talk.</li>
  <li>YOUTUBE LINK is the relevant links, this is okay to leave empty.</li>
  <li>SLIDE_FILENAME_X are the relevant filenames (no "hottestfiles/" prefix necessary), multiple pdfs can be attached to a single talk and should be seperated by a single space. This is okay to leave empty.</li>
  <li>ABSTRACT CONTENT is the abstract, which should be split into lines for the desired paragraph breaks. The abstract can be as long as you would like, but it must always be the last entry.</li>
  <li>HTML can be added to ABSTRACT CONTENT and will be rendered correctly, such as, if you want to include a hyperlink.</li>
</ul>

THINGS THAT WILL AFFECT PAGE GENERATION (indexGenerator.py will throw an exception):
<ul>
  <li>Misspelled line starters</li>
  <li>Improperly formatted term or date entries</li>
  <li>Missing entries (other than youtube link/pdf/school)</li>
  <li>"Abstract:" not being the last entry (the exception that will show up in this case is for missing entries of whatever was below "Abstract:")</li>
  <li>&gt; and &lt; symbols in abstract (must be replaced with &amp;gt; and &amp;lt; to not get following error: yattag.indentation.XMLTokenError) </li>
</ul>

THINGS THAT WILL _NOT_ AFFECT PAGE GENERATION:
<ul>
  <li>File name</li>
  <li>Whitespace differences (either before or after lines, between entry label and content, or general blank lines)</li>
  <li>Capitalization</li>
  <li>Missing youtube link/slides/school</li>
  <li>Ordering of entries (besides "Abstract:" which must go last)</li>
</ul>
