import re
x = 'From stephen.marquard@uct.ac.za Sat'
y = re.findall('@([^ ]*)', x)
print(y)

#@([^ ]* extract after @, match non blank chars, match many of them 

#\$[0-9.]+    '.' is to make the program accept float numbers, $ actually has a meaning but '\' this makes it a string

