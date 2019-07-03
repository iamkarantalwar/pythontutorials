#import tkinter modules in your file
from tkinter import *
#to write message box
from tkinter import messagebox


#create a mainwindow class
class MainWindow:
    #create a constructor
    def __init__(self):
        #make a window 
        self.win = Tk()

        #it is responible for setting and getting text in entrybox
        self.name = StringVar(self.win)

        #this is use to adjust the window size
        self.win.geometry('400x400')

        

        self.pic = PhotoImage(file="log.png")

        self.lab = Label(self.win,image=self.pic)
        self.lab.place(x=20,y=20)

        #these options are for option menu
        option =[
            "Core Python",
            "Django",
            "Data Science"
            ]
     
        #optionmenu is used to limit the options for user

        #self.optval is a variable which is responsible for getting
        #and setting values in option Menu
        self.optval = StringVar(self.win)

        #this is a option menu
        self.opt = OptionMenu(self.win,self.optval,*tuple(option))
        self.opt.place(x=0,y=200)
        #this is used to give bg,fg and font to the optionMenu
        self.opt.config(bg="red",font=('',20))

        self.btn = Button(self.win,text="click me",command=self.fun)
        self.btn.place(x=0,y=300)
        

      
    
        
        #it is use to configure the window
        self.win.config(bg="red")
        
        #it is use to make the window in a loop
        self.win.mainloop()
 
    #this function will invoked after click of a button        
    def fun(self):
        print(self.optval.get())
       
                       
        

    #this function will invoked when we will click the button
    def printmsg(self):
        #it is used to get text from the entrybox
        x = self.name.get()
        #it is used to print message inside the messagebox
        messagebox.showinfo("Title","Here will be your message"+x)
        #it is used to set the entry after displaying the message
        self.name.set("")

 
        
        
#here we create an object so the constructer code will automatically invoked
d = MainWindow()


