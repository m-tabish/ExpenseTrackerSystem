import tkinter as tk
from tkinter import ttk
# from tkmacosx import Button
from tkinter import Button
from PIL import ImageTk, Image
from tkinter import messagebox
# from forex_python.converter import CurrencyRates

root = tk.Tk()
root.title("Prism Expense Tracking System")
root.geometry("1000x740")
root.configure(bg="black")

root.iconphoto(False ,tk.PhotoImage(file= "calculator.png"))
root.resizable(False, False)

#creating global variables for keeping the code modular
global prim_font
global prim_color
global sec_color
global label_x
global btn_x 
global clickBtn_x
prim_font = "Poppins"
prim_color = "black"
sec_color = "#FFD700"
caret_down_gold = ImageTk.PhotoImage(Image.open('ETS_files/caret_down_gold.png'))
label_x = 100
btn_x = 350
clickBtn_x = 740

# TITLE OF THE PAGE
title = tk.Label(root, text = "Currency Convertor",font=(prim_font , 24, "bold"),fg=sec_color,bg=prim_color, pady=5 ).place(x = 330 , y = 30)


conv_amt = tk.DoubleVar()
conv_amt.set(0.0)



#Functions
def update_label():
    input_text = original_amt.get()
    if (input_text.isdigit() == False):
       messagebox.showerror("Python error", "Error: Please enter an integer value")
       
       
    conv_amt.set(input_text)
    
def clear_input():
    original_amt.delete(0,tk.END)


#all box labels
amt_label = tk.Label(root, text = "Amount: ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x=label_x , y= 150)
from_label = tk.Label(root, text = "From : ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x=label_x , y= 250)
to_label = tk.Label(root, text = "To : ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x=label_x, y= 350)
convertedAmt_label = tk.Label(root, text = "Converted  ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x= label_x, y= 550)
convertedAmt_label = tk.Label(root, text = "Amount: ", font=(prim_font,18,"bold"),bg=prim_color, fg=sec_color).place(x= label_x+10, y= 590)


newAmt = tk.Label(
    root,
    textvariable=conv_amt,
    font=(prim_font,18),
    fg=sec_color,
    bg=prim_color,
    borderwidth=0.5,
    # insertbackground= sec_color
    ).place(x= btn_x ,y = 550)



#input boxes
original_amt = tk.Entry(
root,
font=(prim_font,18),
fg=sec_color,
bg=prim_color,
borderwidth=0.5,
insertbackground= sec_color
)
original_amt.place(x= btn_x,y = 150)


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
from_btn.place(x = btn_x, y= 260)



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
to_btn.place(x = btn_x, y= 360)


# Convert and Clear All buttons

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
convert_btn.place(x = clickBtn_x, y= 150)

clear_btn = Button(
    root, 
    text= "Clear All", 
    command = clear_input,
    font =(prim_font,18), 
    fg =sec_color, 
    bg= prim_color, 
    width= 10, 
    height=1, 
    activebackground=sec_color, 
    activeforeground=prim_color,
    ).place(x = clickBtn_x, y= 250)




tk.mainloop()