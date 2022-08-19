#Extracting data from an html page. Opening the third or fourth ...
#href for a lot of times and reading the name written on href

import urllib.request as ur
from bs4 import *

current_repeat_count = 0
url = input('Enter URL: ')
repeat_count = int(input('Enter count:')) #how many times
position = int(input('ENter position: ')) #which hreh

#open the file and read it, extract href tags
def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print('Retrieving: ', url)
    #?
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print('Last Url: ', url)
