import json
import os.path
from os import path

#checks if data info exists, if it loads it if it doesn't it creates a blank object
if path.exists("data.json"):
    with open('data.json') as json_file:
        data = json.load(json_file)
else:
    data = {}
    data['recycle'] = []
    data['trash'] = []
    data['compost'] = []

# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

#save object to file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)