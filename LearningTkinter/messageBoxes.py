from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


root  = Tk()
root.geometry("1440x900")



def popup():
    
    #showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    
    response = messagebox.askyesno("this is messagebox", "hello world")
    Label(root, text = response).pack()
    if response == 1:
        Label(root, text= 'you clicked yes').pack()
    else:
        Label(root, text= 'you clicked no').pack()
Button(root, text = "Popup", command = popup).pack()

mainloop()