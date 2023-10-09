import tkinter as tk
# from tkinter import *
from tkinter import ttk
# from tkmacosx import Button
from tkinter import Button
from PIL import ImageTk, Image


root = tk.Tk()
root.title("Team DevDuo/DebuggingDuo/Dev-N-Debug")
root.geometry("1500x740")
root.configure(bg="black")
root.resizable(False, False)

#creating global variables for keeping the code modular
global prim_font
global prim_color
global sec_color
prim_font = "Poppins"
prim_color = "black"
sec_color = "#FFD700"
caret_down_gold = ImageTk.PhotoImage(Image.open('ETS_files/caret_down_gold.png'))

# TITLE OF THE PAGE
title = tk.Label(root, text = "Currency Convertor",font=(prim_font , 24, "bold"),fg=sec_color,bg=prim_color, pady=5 ).place(x = 630 , y = 30)




#all box labels
amt_label = tk.Label(root, text = "Amount: ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x= 300,y= 150)
from_label = tk.Label(root, text = "From : ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x= 300,y= 250)
to_label = tk.Label(root, text = "To : ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x= 300,y= 350)
convertedAmt_head = tk.Label(root, text = "Converted Amount : ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x= 300,y= 550)


#functions

conv_amt = tk.IntVar()
conv_amt.set(0.0)

def update_label():
    input_text = original_amt.get()
    conv_amt.set(input_text)
    



#input boxes
original_amt = tk.Entry(
root,
font=(prim_font,18),
fg=sec_color,
bg=prim_color,
borderwidth=0.5,
insertbackground= sec_color
)
original_amt.place(x= 600,y = 150)



newAmt = tk.Label(
    root,
    textvariable=conv_amt,
    font=(prim_font,18),
    fg=sec_color,
    bg=prim_color,
    borderwidth=0.5,
    # insertbackground= sec_color
    ).place(x= 600,y = 550)



#currency list 
currency_list = [
    "Indian Rupees (INR)",
    "USA Dollar	 (USD)",
    "Afghanistan Afghani (AFN)",
    "Albania Lek (ALL)", 
    "Algeria Dinar (DZD)",
    "Angola Kwanza (AOA)",
    "United Arab Emirates Dirham	AED"   
    
]


#Drop down button 1
from_btn_default = tk.StringVar()
from_btn_default.set( "Select")
from_btn = tk.OptionMenu(root, from_btn_default, *currency_list)

def resize_btn():
    global width_btn
    width_btn = tk.IntVar()
    width_btn.set(len(from_btn.get()))
     
from_btn.config(
    fg = sec_color,
    bg = prim_color,     
    activeforeground= prim_color,
    activebackground= sec_color,
    border =0,
    highlightbackground= sec_color,
    highlightthickness=0.5,
    indicatoron=0,
    font=(prim_font, 13),
    width = 22,
    compound = tk.RIGHT ,#displays the caret down image to the right
    # image = caret_down_gold
)
from_btn["menu"].config(
    fg = sec_color,
    bg = prim_color,
    font =(prim_font, 12),
    activeborder= 0,
    border=0
)
from_btn.place(x = 630, y= 260)



#Drop down button 2

to_btn_default = tk.StringVar()
to_btn_default.set( "Select")
to_btn = tk.OptionMenu(root, to_btn_default, *currency_list)
to_btn.config(
    fg = sec_color,
    bg = prim_color,     
    activeforeground= prim_color,
    activebackground= sec_color,
    border =0,
    highlightbackground= sec_color,
    highlightthickness=0.5,
    indicatoron=0,
    font=(prim_font, 13),
    # image = caret_down_gold,
    width = 22,
    compound = tk.RIGHT #displays the caret down image to the right
)
to_btn["menu"].config(
    fg = sec_color,
    bg = prim_color,
    font =(prim_font, 12),
    activeborder= 0,
    border=0
)
to_btn.place(x = 630, y= 360)


#Other call to action buttons (CTA)

convert_btn = tk.Button(
    root, 
    text= "Convert", 
    command = update_label,
    font =(prim_font,18), 
    fg =sec_color, 
    bg= prim_color,
    width= 10, 
    height=1,
    activebackground=sec_color,
    activeforeground=prim_color
    )
convert_btn.place(x = 1000, y= 150)

clear_btn = Button(
    root, 
    text= "Clear All", 
    font =(prim_font,18), 
    fg =sec_color, 
    bg= prim_color, 
    width= 10, 
    height=1, 
    activebackground=sec_color, 
    activeforeground=prim_color,
    ).place(x = 1000, y= 250)




tk.mainloop()