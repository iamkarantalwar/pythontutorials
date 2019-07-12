from tkinter import *
import db
class MainWindow:
    def __init__(self):
        self.root = Tk()

        
        self.lab = Label(self.root,text="Name")
        self.lab.place(x=0,y=0)
        self.lab = Label(self.root,text="Email")
        self.lab.place(x=0,y=40)
        self.lab = Label(self.root,text="Password")
        self.lab.place(x=0,y=80)

        self.name = StringVar(self.root)
        self.email = StringVar(self.root)
        self.password = StringVar(self.root)

        self.ent  = Entry(self.root,textvariable=self.name)
        self.ent.place(x=80,y=0)
        self.ent  = Entry(self.root,textvariable=self.email)
        self.ent.place(x=80,y=40)
        self.ent  = Entry(self.root,textvariable=self.password)
        self.ent.place(x=80,y=80)

        self.btn = Button(self.root,text="Add Data",command=self.hello)
        self.btn.place(x=120,y=120)
        self.root.mainloop()

    def hello(self):
        lis = [self.name.get(),
               self.email.get(),
               self.password.get()]
        db.insertData(lis)
        
        print("button has been clicked")

d = MainWindow()
