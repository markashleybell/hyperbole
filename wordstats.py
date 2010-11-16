import urllib, re
from operator import itemgetter
from BeautifulSoup import BeautifulSoup, NavigableString

file = urllib.urlopen('http://www.dailymail.co.uk/home/index.html')
html = file.read()
file.close()

soup = BeautifulSoup(html)
text = [t.text for t in soup.findAll(['p', 'h1', 'h2', 'span', 'li'])]
words = re.sub('[^a-zA-Z0-9\-\s]', '', ' '.join(text)).split(' ')

wordcount = {}

for word in words:
    w = word.lower()
    if(w not in wordcount):
        wordcount[w] = 0
    wordcount[w] += 1
    
sorted = sorted(wordcount.items(), key=itemgetter(1), reverse=True)

for s in sorted:
    if s[1] > 10:
        print s[0] + ': ' + str(s[1])