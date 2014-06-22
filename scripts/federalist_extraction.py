# This script downloads the Federalist Papers text file found at
# (http://www.gutenberg.org/ebooks/18.txt.utf-8) and then extracts the separate
# documents and saves them in their own files.

import os
import re
import urllib2

DATA = os.environ['DATA']
ME = 'thomas'
MYDATA = os.path.join(DATA, ME, 'authorship_federalist')
PROCESSED = os.path.join(MYDATA, 'processed')
RAW = os.path.join(MYDATA, 'raw')
SEPARATED = os.path.join(PROCESSED, 'separated')

for directory in [RAW, SEPARATED]:
    try:
        os.makedirs(directory)
    except OSError: # In case directory already exists.
        pass

# Download the Federalist Papers.
federalist_url = 'http://www.gutenberg.org/ebooks/18.txt.utf-8'
response = urllib2.urlopen(federalist_url)
text = response.read()

federalist_path = os.path.join(RAW, 'federalistpapers.txt')
with open(federalist_path, 'w') as f:
    f.write(text)

# Reopen file to deal with line-ending issues.
with open(federalist_path) as f:
    federalistdoc = f.readlines()

exp = '^FEDERALIST\.? No\.? \d+'
regex = re.compile(exp)

# Find line numbers where different federalist papers start.
index = []
for num, line in enumerate(federalistdoc):
    if regex.match(line):
        index.append((line, num))

# Find line ranges of each federalist document.
ranges = []
for i in range(len(index)):
    try:
        ranges.append((index[i][0], index[i][1], index[i + 1][1]))
    except IndexError: # Deal with final document.
        ranges.append((index[i][0], index[i][1], len(federalistdoc)))

# The 70th federalist paper has two versions and must be especially treated so
# that one is saved as '70a.txt' and the other is saved as '70b.txt'.
found70 = False
for title, low, high in ranges:
    num = re.findall('\d+', title)[0]
    num = num.zfill(2)

    if num == '70':
        if found70:
            num += 'b'
        else:
            num += 'a'
            found70 = True

    filename = os.path.join(SEPARATED, num + '.txt')
    with open(filename, 'w') as f:
        f.writelines(federalistdoc[low: high])
