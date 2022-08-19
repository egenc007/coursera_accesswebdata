import re
hand = open('rex.txt')
for line in hand:
    line.rstrip()
    if re.search('^students', line):
        print(line)

#^X.*: starts with X and it will be followed by number of chars followed by :

#^X-\S+: STartswith X- match any non-whitespace chars one or more times

