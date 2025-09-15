#!/usr/bin/env python3

# Given a single argument of the form TermYYYY.txt, it reads the file
# TermInfo/TermYYYY.txt.  Here YYYY is a four-digit year and Term is
# usually Fall or Winter.
#
# For each line in that file, it generates a file in the TalkInfo
# folder.  The lines in the input are of the form
#
#   First Last; MMM DD; affiliation
#
# "First Last" could include middle names or other connectives.
# MMM is a three letter month like Jan, Feb, etc.
# DD is a one- or two-digit day of the month.
#
# From this line, it would generate a file named FirstLast-MMMDD.txt
# (with all spaces removed from the name and possibly one or two digits).
#
# The contents of the file would be:
#
# Term: Term YYYY
# Date: MON DD
# Speaker: First Last
# School: affiliation
# Title:
# YouTube:
# Slides:
# Abstract:

import os
import sys

def generate_talk_files(term):
    term_name = term[:-4] + ' ' + term[-4:]
    input_path = os.path.join("TermInfo", term + '.txt')

    # Read the input file
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create output directory if it doesn't exist
    os.makedirs("TalkInfo", exist_ok=True)

    # Process each line
    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            speaker, date, affiliation = [part.strip() for part in line.split(";")]
            month, day = date.split()
            day = str(int(day))  # Remove leading zero if present
        except ValueError:
            print(f"Skipping malformed line: {line}")
            continue

        content = (
            f"Term: {term_name}\n"
            f"Date: {month} {day}\n"
            f"Speaker: {speaker}\n"
            f"School: {affiliation}\n"
            f"Title:\n"
            f"YouTube:\n"
            f"Slides:\n"
            f"Abstract:\n"
        )

        # Create filename and content
        filename = f"{speaker.replace(' ', '')}-{month}{day}.txt"
        filepath = os.path.join("TalkInfo", filename)

        if os.path.exists(filepath):
            print('File exists and left unchanged:', filepath)
            continue

        # Write to file
        with open(filepath, 'w', encoding='utf-8') as out_file:
            out_file.write(content)
        print('File written:', filepath)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: termGenerator.py TermYYYY")
    else:
        generate_talk_files(sys.argv[1])
