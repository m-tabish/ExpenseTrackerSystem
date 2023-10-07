from tkinter import *
root = Tk()
root.title("Tabish")
root.geometry("1440x1000")

# r = IntVar()
# r.set("2")
# Radiobutton(root, text = "INR", variable =r , value =1, command = lambda: clicked(r.get())).pack()
# Radiobutton(root, text = "Select", variable =r , value =2, command = lambda: clicked(r.get())).pack()

Modes = [
    ("Pepporoni ","Pepporoni"), 
    ("Mushroom","Mushroom"),
    ("Tomato","Tomato"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepporoni")

for text, mode in Modes: 
    Radiobutton(root, text = text, variable = pizza , value = mode).pack()

def clicked(value):
    myLabel = Label(root, text = value)
    myLabel.pack()

myLable  = Label(root, text="Click me!", command = lambda: clicked(pizza.get()))
myLable.pack()
root.mainloop()