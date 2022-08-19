#maps.googleapi.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI
#Above url is an example

import urllib.request, urllib.parse, urllib.error
import json as js

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    #Enter the location if its smaller than 1 break the loop
    address = input('Enter location:')
    if len(address) < 1 : break
    url = serviceurl + urllib.parse.urlencode(
        {'address': address})
    print('Retrieving', url)

    #Read the data and retrieve how many chars are there
    uh = urllib.request.urlopen(url)
    data = uh.read().encode()
    print('Retrieved', len(data), 'characters')

    #download the data thats json so that we can play with it in python
    try:
        js = js.loads(data)
    except:
        js = None

    #error code
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===Failure to Retrieve===')
        print(data)
        continue
    #this makes the program show the whole datathats in 4 indent
    #dumps is negative of loads
    print(js.dumps(js, indent=4))

    #finding the data
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print("lat", lat, "lng", lng)

    location = js['results'][0]['formatted_address']
    print(location)