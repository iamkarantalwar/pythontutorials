from tkinter import *

class Main:
    def __init__(self):
        self.tk = Tk()
        #this piece of code is used to find screen height and width
        x = self.tk.winfo_screenheight()
        y = self.tk.winfo_screenwidth()

        print(x,y)
        #this piece of code is used to find out the center co ordinates
        height= (x-600)//2
        width = (y-600)//2

        #this piece of code is used to make the screen in center
        self.tk.geometry('600x600+{}+{}'.format(str(width),str(height)))

        #this is used to upload image in the tkinter libraryW
        self.img = PhotoImage(file="obama.gif")

        #this will create the canvas exactly equal to the window size
        self.canvas = Canvas(self.tk,height=600,width=600,bg="red")

        #this is used to create the image inside the canvas
        self.canvas.create_image(0,0,anchor='nw',image=self.img)

        #this is used to create the canvas text
        self.canvas.create_text(30,30,text="Hello",fill="white",font=('',20))

        #this is used to place the canvas
        self.canvas.place(x=0,y=0)
        #this is used to restrict the window from resizing
        self.tk.resizable(height=False,width=False)

        self.tk.mainloop()


d = Main()
