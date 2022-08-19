#reading files
import urllib.request, urllib.parse, urllib.error

#to make it read html files you should do page.html instead of romeo.txt
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())