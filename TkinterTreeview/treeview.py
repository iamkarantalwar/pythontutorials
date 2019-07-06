from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import getdata
class Window:
    def __init__(self):

        self.tk = Tk()
        self.tk.geometry('500x500')
        fetch= (getdata.fetch())
        self.tree = Treeview(self.tk,columns=("#1","#2"))
        self.tree.heading("#0",text="user id")
        self.tree.column("#0",width=60)
        self.tree.heading("#1",text="User Name")
        self.tree.heading("#2",text="Password")
        for i in fetch:
            self.tree.insert('','end',text=i[0],values=(i[1],i[2]))
        self.tree.place(x=0,y=0)

        self.tree.bind("<Double-Button-1>",self.popupdata)

        self.tk.bind("<Control-o>",self.trigger)

    def popupdata(self,e):
        print(e)
        messagebox.showinfo("title","Event is triggered")

    def trigger(self,e):
        print("Control o has been pressed")
        
        
        

        



d = Window()

