from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import getdata
class Window:
    def __init__(self):

        self.tk = Tk()
        self.tk.geometry('500x500')
        fetch= (getdata.fetch())
        self.tree = Treeview(self.tk,columns=("#1","#2","#3","#4"))
        self.tree.heading("#0",text="user id")
        self.tree.column("#0",width=60)
        self.tree.heading("#1",text="User Name")
        self.tree.heading("#2",text="Password")
        self.tree.heading("#3",text="Update")
        self.tree.heading("#4",text="Delete")
        self.data = getdata.fetch()
        for i in self.data:
            self.tree.insert('','end',text=i[0],values=(i[1],i[2],"update","delete"))
        self.tree.place(x=0,y=0)
        
        

        self.tree.bind("<Double-Button-1>",self.trigger)     

        

        self.tk.mainloop()

    
        
        

    def trigger(self,e):
        #e will identify from where the function has been triggered
        print(e)
        #d will store the object of focused element in the treeview
        d = self.tree.focus()
        #self.tree.item is use to get the data from the focused row
        #so thats why we pass the focused item there d
        x = (self.tree.item(d))
        print(x)
        #col will identify the focused column
        col = self.tree.identify_column(e.x)
        if col=="#3":
            
            print("Update")
        elif col == "#4":
            getdata.delete(x["text"])
            print("delete")
        
        
        

        



d = Window()

