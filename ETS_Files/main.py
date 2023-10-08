import tkinter as tk
# from tkinter import *
from tkinter import ttk
# from tkmacosx import Button
from tkinter import Button
from PIL import ImageTk, Image


root = tk.Tk()
root.title("Team DevDuo/DebuggingDuo/Dev-N-Debug")
root.geometry("1500x840")
root.configure(bg="black")

#creating global variables for keeping the code modular
global prim_font
global prim_color
global sec_color
prim_font = "Poppins"
prim_color = "black"
sec_color = "#FFD700"
# caret_down_black = ImageTk.PhotoImage(Image.open('caret_down_black50x50.png'))

#creating the title outside the main frame
frame_width = 840
title = tk.Label(root, text = "Currency Convertor",font=(prim_font , 18),fg=sec_color,bg=prim_color ).place(relx = 0.5 , anchor = tk.N)
#row =0, column=3, columnspan=4



#inserting elements in main frame 
amt_label = tk.Label(root, text = "Amount: ", font=(prim_font,18),bg=prim_color, fg=sec_color).place(x= 300,y= 100)
From_label = tk.Label(root, text = "From: ", font=(prim_font,18),bg=prim_color, fg=sec_color).place(x= 300,y= 200)

#input box to enter amount
amt_input = tk.Entry(root,font=(prim_font,18),fg=sec_color,bg=prim_color,borderwidth=0.5).place(x= 600,y = 100)

#  inserting 2 drop down buttons to select currency

currency_list = [
    "Indian Rupees (INR)",
    "USA Dollar	 (USD)",
    "Afghanistan Afghani (AFN)",
    "Albania Lek (ALL)", 
    "Algeria Dinar (DZD)",
    "Angola Kwanza (AOA)"   
    
]
from_btn_default = tk.StringVar()
from_btn_default.set( "Select")
from_btn = tk.OptionMenu(root, from_btn_default, *currency_list)
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
    width = 15
    # image = caret_down_black
)
from_btn["menu"].config(
    fg = sec_color,
    bg = prim_color,
    font =(prim_font, 12),
    activeborder= 0,
    border=0
)
from_btn.place(x = 630, y= 210)

#inserting convert button
convert_btn = Button(root, text= "Convert", font =(prim_font,18), fg =sec_color, bg= prim_color, width= 10, height=1 ).place(x = 1000, y= 100)
clear_btn = Button(root, text= "Clear All", font =(prim_font,18), fg =sec_color, bg= prim_color, width= 10, height=1 ).place(x = 1000, y= 200)

#inserting drop down button 
# btn = tk.OptionMenu(root, "button", value = 1).place(x = 1000, y= 100)
tk.mainloop()