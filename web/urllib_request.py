#!/usr/bin/env python3

import urllib.parse
import urllib.request

url = "http://www.fud.edu.ng/cgi-bin/register.cgi"

values = {
    'name': 'Muhammad S. Ali',
    'location': 'Dutse',
    'language': 'Python'
}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    the_page = response.read().decode('utf-8')

print("The Result: ----------------------------------------")
print(the_page)

