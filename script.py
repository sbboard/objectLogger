import json
import os.path
from os import path
from tkinter import *
from PIL import ImageTk, Image

window = Tk()

window.title("Prop Registration Tool")

load = Image.open("temp.gif")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.grid(column=0, row=0,rowspan = 3)

lbl = Label(window, text="item unidentified", font=("Arial Bold", 50))
lbl.grid(column=1, row=0)

btn = Button(window, text="Register",font=("Arial Bold", 50), bg="white", fg="blue")
btn.grid(column=1, row=1)

closingMsg = Label(window, text="tool will close in 10", font=("Arial Bold", 30))
closingMsg.grid(column=1, row=2)

window.mainloop()
# potentItems = ["flower","banana","blade"]

# def numInput():
#     number = -1
#     tries = 0
#     while int(number) < 0 or int(number) >= len(potentItems):
#         number = input()
#         tries += 1
#         if tries > 0: 
#             print("please select a number between",0,"and",len(potentItems)-1)
#     else: return number

# def yes_or_no(question):
#     while "the answer is invalid":
#         reply = str(input(question+' (y/n): ')).lower().strip()
#         if reply[0] == 'y':
#             return True
#         if reply[0] == 'n':
#             return False

# def saveObj():
#     ID = input('Scan RFID Chip:')
#     print("What item is this prop?")
#     for index, x in enumerate(potentItems):
#         print(index, x)
#     prop = numInput()
#     data['tags'].append({
#         'ID': ID,
#         'Prop': prop
#     })
#     with open('data.json', 'w') as outfile:
#         json.dump(data, outfile)
#     print("object saved")
#     if yes_or_no("scan another object?"):
#         saveObj()

# #checks if data info exists, if it loads it if it doesn't it creates a blank object
# if path.exists("data.json"):
#     with open('data.json') as json_file:
#         data = json.load(json_file)
# else:
#     data = {}
#     data['tags'] = []

# saveObj()