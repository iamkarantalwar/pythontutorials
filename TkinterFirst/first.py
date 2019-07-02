#import tkinter modules in your file
from tkinter import *

#create a mainwindow class
class MainWindow:
    #create a constructor
    def __init__(self):
        
        #make a window 
        self.win = Tk()
        
        #this is use to adjust the window size
        self.win.geometry('400x100')
        
        #this is use the give the title to the window
        self.win.title("My First Window")
        
        #this is use to write the text
        #fg is use to color the label
        #bg is use to color the background
        #font is use to change the font of the label
        self.label = Label(self.win,text="My First WIndow",bg="white",fg="blue",font=('arial',20))

        #we have to place the label by telling the distance from x axis and y axis
        self.label.place(x=100,y=60)

        #it is use to configure the window
        self.win.config(bg="red")

        #it is use to make the window in a loop
        self.win.mainloop()
        
#here we create an object so the constructer code will automatically invoked
d = MainWindow()


