import re 
x = 'My 2 favorite numbers are 19 and 42.'
y = re.findall('[0-9]+', x)
print(y)

#['2', '19', '42']
#[0-9]+   means and integer one or more digits

#[AEIOU]+   means one or more capital vowel

#^F.+: one or more chars.   Tries to print out the largest output as possible
#^F.+? one or more chars.   prints out the shortest output as possible
