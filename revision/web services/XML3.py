#Gets data from a XML page

import urllib.request as ur
import xml.etree.ElementTree as ET

url = input('Enter location: ')
total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = ET.fromstring(xml)
#.//count means find count tag
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum', sum)