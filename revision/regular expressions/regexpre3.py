import re
x = 'From stephen.marquard@uct.ac.za Sat'
y = re.findall('\S+@\S+', x)
print(y)

#['stephen.marquard@uct.ac.za'].    \S+@\S+ there has to be non-whitespace chars around the @.

#'^From (\S+@\S+)'   starts with From but () means just print out whatever is between brackets.

