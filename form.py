
#!/usr/bin/python

import requests

data1 = {'name': 'Robert', 'city': 'Oregon'}
data2 = {'method' : 'creditcard', 'total': 100}
url1 = 'http://yourserver/checkout1.php'
url2 = 'http://yourserver/checkout2.php'

req1 = requests.post(url1, data=data1)
req2 = requests.post(url2, data=data2)  

# in certain condition, you may need to login before you can post the data.
# to do this, you can use requests.session() to create persistent session after login action.
# see http://docs.python-requests.org/en/latest/user/advanced/#session-objects
