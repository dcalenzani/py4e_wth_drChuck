import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
counts = dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#largest key
largest = -1
wordinho = None
for k,v in counts.items() :
    if v > largest:
        largest = v
        wordinho = k
print('the largest word is "', wordinho, '" and it repeats' , largest, ' times' )