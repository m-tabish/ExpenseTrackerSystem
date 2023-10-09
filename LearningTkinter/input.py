from tkinter import *
 
root =  Tk()

e = Entry(root, width="100")
e.pack()
e.insert(0, "enter your name") #enters a placeholder in the input box



def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command= myClick,fg = "white", bg="#ff0000")
myButton.pack()

root.mainloop()
