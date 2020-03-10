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
selectedItem = ""

def saveObj():
    ID = input('Scan RFID Chip:')
    print("What item is this prop?")
    #for index, x in enumerate(potentItems):
    #    print(index, x)
    data['tags'].append({
        'ID': ID,
        'Prop': prop
    })
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    print("object saved")

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
        for F in (StartPage, PageOne, PageTwo, PageThree):
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
            global recycle
            global trash
            global compost
            if selectedCat == 'recycle':
                currArray = recycle
            elif selectedCat == 'trash':
                currArray = trash
            elif selectedCat == 'compost':
                currArray = compost
            for index, x in enumerate(currArray):
                print(index, x)
                buttonArray[index]['text'] = x
            label['text'] = ("which",selectedCat,"object?")
        def saveObj(self):
            print('save')
            self.controller.show_frame("PageThree")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="wild", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",command=lambda:saveObj(self))
        button.pack()
        button2 = tk.Button(self, text="Go to the start page",command=lambda:saveObj(self))
        button2.pack()
        button3 = tk.Button(self, text="Go to the start page",command=lambda:saveObj(self))
        button3.pack()
        buttonArray = [button,button2,button3]
        self.bind("<<ShowFrame>>", on_show_frame)

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Saved!", font=self.controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
if path.exists("data.json"):
    with open('data.json') as json_file:
        data = json.load(json_file)
else:
    data = {}
    data['tags'] = []

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()