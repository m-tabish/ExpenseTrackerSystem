from tkinter import *
 
root =  Tk()


#creating a label widget
myLable1 = Label(root, text= "hello World!")
myLabel2 = Label(root, text= "My name is Tabish")

#shoving it onto the screen
myLable1.grid(row=0, column =0)
myLabel2.grid(row=1, column =1)


root.mainloop()
