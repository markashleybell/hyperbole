import urllib, re, sys
from operator import itemgetter
from BeautifulSoup import BeautifulSoup, NavigableString

# Get the list of stop words from our text file
file = open('stopwords.txt', 'r')
# Remember to strip the newline characters so they match our words
stopwords = [str(line).rstrip() for line in file]

# Get the raw HTML
page = urllib.urlopen('http://www.dailymail.co.uk/home/index.html')
html = page.read()
page.close()

soup = BeautifulSoup(html)
# Get the text from specific tags
text = [t.text.strip() for t in soup.findAll(['p', 'h1', 'h2', 'span', 'li'])]
# Remove all punctuation except hyphens and apostrophes
words = re.sub('\s\'|\'\s', '', re.sub('[^a-zA-Z0-9\-\s]', '', ' '.join(text))).split(' ')

wordcount = {}

for word in words:
    w = word.lower()
    if w not in stopwords: # If it's a stop word, ignore it
        if w not in wordcount: # If we haven't already seen the word
            wordcount[w] = 0 # Add it to the dictionary
        wordcount[w] += 1 # Increment the total occurrences
    
# Get a list of the items sorted by descending value (occurrences)
sorted = sorted(wordcount.items(), key=itemgetter(1), reverse=True)

# Show everything with more than 5 occurrences
for s in sorted:
    if s[1] > 0:
        print s[0] + ': ' + str(s[1])