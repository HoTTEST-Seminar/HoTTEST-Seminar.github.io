#!/usr/bin/env python3

# Given a single argument of the form TermYYYY.txt, we read the file
# TermInfo/TermYYYY.txt.  Here YYYY is a four-digit year and Term is
# usually Fall or Spring.  We assume the usual start and end times.
# You can edit the .csv output file manually if needed.
#
# The output is a file CalendarInfo/TermYYYY.csv, containing one
# row for each line of TermYYYY.txt.  The csv file can be imported
# into Google Calendar to create the calendar entries.
#
# Note:  If you import it a second time, it will create duplicate
# entries.
#
# The lines in the input are of the form
#
#   First Last; MMM DD; affiliation
#
# "First Last" could include middle names or other connectives.
# MMM is a three letter month like Jan, Feb, etc.
# DD is a one- or two-digit day of the month.

import os
import sys
import csv
from datetime import datetime

def generate_calendar(term, force=False):
    year = term[-4:]
    input_path = os.path.join("TermInfo", term + '.txt')

    # Read the input file
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create output directory if it doesn't exist
    os.makedirs("CalendarInfo", exist_ok=True)

    filepath = os.path.join("CalendarInfo", term+'.csv')

    if not force and os.path.exists(filepath):
        print('File exists and left unchanged (use -f to overwrite):', filepath)
        return

    writer = csv.writer(open(filepath, 'w'))
    print('Saving output to', filepath)

    head = ['Subject', 'Start Date', 'Start Time', 'End Date', 'End Time', 'Location']
    writer.writerow(head)

    # Process each line
    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            speaker, date, affiliation = [part.strip() for part in line.split(";")]
            month, day = date.split()
            month = datetime.strptime(month, '%b').strftime('%m') # Two-digit string, 01 to 12.
            day = '%02d' % (int(day),)  # Add leading zero if needed.
        except ValueError:
            print(f"Skipping malformed line: {line}")
            continue

        row = [speaker + ', HoTTEST',
               '%s-%s-%s' % (year, month, day),
               '11:30 AM',
               '%s-%s-%s' % (year, month, day),
               '1:00 PM',
               'https://zoom.us/j/994874377']

        writer.writerow(row)

    print("Output file can be imported into Google Calendar.")

if __name__ == "__main__":
    if len(sys.argv) == 2 or (len(sys.argv) == 3 and sys.argv[1] == '-f'):
        force = (len(sys.argv) == 3)
        generate_calendar(sys.argv[-1], force=force)
    else:
        print("Usage: calendarGenerator.py [-f] TermYYYY")
