import json
import os.path
from os import path

def numInput():
	number = input("What category is this item in?:")
	if number.isdigit():
		return number
	else:
		print("You must enter a number (i.e. 0,1,2...)")
		numInput()

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def saveObj():
    ID = input('Scan RFID Chip:')
    prop = numInput()
    data['items'].append({
        'ID': ID,
        'Prop': prop
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    print("object saved")
    if yes_or_no("scan another object?"):
        saveObj()

#checks if data info exists, if it loads it if it doesn't it creates a blank object
if path.exists("data.json"):
    with open('data.json') as json_file:
        data = json.load(json_file)
else:
    data = {}
    data['items'] = []

saveObj()