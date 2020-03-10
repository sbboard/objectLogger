import tkinter as tk
from tkinter import font  as tkfont
import json
import os.path
from os import path
from PIL import ImageTk, Image

objectToRegister = "okokokok"
recycle = ["paper","cardboard","milk"]
trash = ["rubber","bone","blade"]
compost = ["flower","banana","egg"]
selectedCat = ""

def numInput():
    number = -1
    tries = 0
    while int(number) < 0 or int(number) >= 3:
        number = input()
        tries += 1
        if tries > 0: 
            print("please select a number between",0,"and",2)
    else: return number

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def saveObj():
    ID = input('Scan RFID Chip:')
    print("What item is this prop?")
    #for index, x in enumerate(potentItems):
    #    print(index, x)
    prop = numInput()
    data['tags'].append({
        'ID': ID,
        'Prop': prop
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    print("object saved")
    if yes_or_no("scan another object?"):
        saveObj()

#wrap
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")

# option to register
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("temp.gif")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(image=render)
        img.image = render
        #img.pack()
        lbl = tk.Label(self, text="item unidentified", font=("Arial Bold", 50))
        lbl.pack()
        btn = tk.Button(self, text="Register",font=("Arial Bold", 50), bg="white", fg="blue",command=lambda: controller.show_frame("PageOne"))
        btn.pack()
        closingMsg = tk.Label(self, text="tool will close in 10", font=("Arial Bold", 30))
        closingMsg.pack()
        self.bind("<<ShowFrame>>", self.on_show_frame)
    def on_show_frame(self,event):
        print("I am being shown...")

#choose category
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        def nextPage(self,cat):
            global selectedCat 
            selectedCat = cat
            self.controller.show_frame("PageTwo")
        tk.Frame.__init__(self, parent)
        self.update()
        self.controller = controller
        label = tk.Label(self, text="Object Category:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Recycle", command=lambda: nextPage(self,'recycle'))
        button2 = tk.Button(self, text="Trash", command=lambda:nextPage(self,'trash'))
        button3 = tk.Button(self, text="Compost", command=lambda:nextPage(self,'compost'))
        button.pack()
        button2.pack()
        button3.pack()   
        self.bind("<<ShowFrame>>", self.on_show_frame)
    def on_show_frame(self,event):
        print("I am being shown...")   

#choose object
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        def on_show_frame(self):
            global selectedCat
            print("ok")
            label['text'] = selectedCat
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="wild", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        button.pack()
        self.bind("<<ShowFrame>>", on_show_frame)
        
if path.exists("data.json"):
    with open('data.json') as json_file:
        data = json.load(json_file)
else:
    data = {}
    data['tags'] = []

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()