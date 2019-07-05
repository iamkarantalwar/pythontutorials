from tkinter import *
from tkinter import messagebox
#it will import the mydb.py which will be in your current folder
import mydb

class Main:
    def __init__(self):
        self.tk = Tk()

        #these are responsible for getting and set text inside the entry boxes
        self.user = StringVar(self.tk)
        self.passw = StringVar(self.tk)
        
        self.label = Label(self.tk,text="username")
        self.label.place(x=0,y=0)

        self.entry = Entry(self.tk,textvariable=self.user)
        self.entry.place(x=60,y=0)

        self.label = Label(self.tk,text="password")
        self.label.place(x=0,y=30)

        self.entry = Entry(self.tk,textvariable=self.passw,show="*")
        self.entry.place(x=60,y=30)

        self.btn = Button(self.tk,text="Click Me",command=self.insert)
        self.btn.place(x=20,y=50)

        self.tk.mainloop()
        
    #it will invoke when click me is clicked
    def insert(self):
        #make a tuple to send the data to the api
        tupl = (self.user.get(),self.passw.get())
        #execute the insert logic which you made in mydb.py
        mydb.insert(tupl)
        #it will show the messagebox
        messagebox.showinfo("Inserted","Your Data has been inserted")
        #it will set the entry to empty string
        self.user.set("")
        self.passw.set("")


d = Main()
        
