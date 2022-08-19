import xml.etree.ElementTree as ET

data = ''' <person>
    <name>Chuck</name>
    <phone type = "intil">
        +1 734 303 4456
    </phone>
    <email hide = "yes" />
</person>'''

tree = ET.fromstring(data)
#finds and gets the text or attribute
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get("hide"))
