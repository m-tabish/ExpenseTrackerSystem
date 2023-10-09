from tkinter import *
 
root =  Tk()


def myClick():
    myLabel = Label(root, text="This button has been clicked")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command= myClick,fg = "white", bg="#ff0000")
myButton.pack()

root.mainloop()
