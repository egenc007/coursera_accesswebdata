import json as js

input = '''[
    {"id": "001",
    "x": "7",
    "name": "Chuck"
    },
    {"id": "009",
    "x": "7", 
    "name": "Chuck"
    }
]'''

info = js.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])