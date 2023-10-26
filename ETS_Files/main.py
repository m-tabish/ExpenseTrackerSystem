import tkinter as tk
from tkinter import ttk
from tkinter import Button
from PIL import ImageTk, Image
from tkinter import messagebox
from forex_python.converter import CurrencyRates

root = tk.Tk()
root.title("Prism Office")
root.geometry("1000x740")
img = tk.PhotoImage(
    False, file="D:\ExpenseTrackerSystem\ETS_Files\PrismOfficeLogo.png")
root.iconphoto(False, img)
root.resizable(False, False)


# creating global variables for keeping the code modular
global prim_font
global prim_color
global sec_color
global label_x
global btn_x
global clickBtn_x
prim_font = "Poppins"
prim_color = "black"
sec_color = "#FFD700"
label_x = 100
btn_x = 350
clickBtn_x = 740


# currency dictionary
currency_rate = {
    "INR": 1,
    "USD": 83.20,
    "EUR": 87.83,
    "AED": 22.65
}


# creating tabs
notebook = ttk.Notebook(root)  # widget that manages collection of windows
Office = tk.Frame(notebook)
Scanner = tk.Frame(notebook)
Office.configure(bg="black")
notebook.add(Office, text="OFFICE")
notebook.add(Scanner, text="Scanner")
notebook.pack(expand=True, fill="both")

# TITLE OF THE PAGE
title = tk.Label(Office, text="Currency Convertor", font=(
    prim_font, 24, "bold"), fg=sec_color, bg=prim_color, pady=5).place(x=330, y=30)
# Functions


def update_label():
    amount = original_amt.get()
    from_currency = currency_rate["INR"]
    to_currency = to_btn_var.get()

    if (amount.isdigit() == False):
        messagebox.showerror(
            "Python error", "Error: Please enter an integer value")
    elif (from_currency == "Select" or to_currency == "Select"):
        messagebox.showwarning("Python error", "Please select the currency")
    else:
        # if(from_currency in currency_rate):

        amount = float(amount)
        result = currency_rate[to_currency] * amount
        converted_amount = result

    conv_amt.set(converted_amount)


def clear_input():
    original_amt.delete(0, tk.END)
    conv_amt.set("0.0")

def open_cal():
    Calculator = tk.Toplevel()
    Calculator.geometry("390x650")
    Calculator.config(bg="black")
    # CALCULTOR'S CODE in this function
    
    # calc = tk.Toplevel()
    expression = ''
    
    
    def show(val):
        global expression
        expression += val
        l2.config(text=expression)
    
    
    def clear():
        global expression
        expression = ''
        l2.config(text=expression)
    
    
    def cal():
        result = ''
        global expression
        if expression != '':
            try:
                result = str(eval(expression))
                expression = result
            except:
                messagebox.showwarning(
                    'Invalid', 'Invalid Operators and number use -_-')
                result = 'error'
                expression = result
        l2.config(text=expression)
    
    
    l2 = tk.Label(Calculator, text='', font=(
        'Helvetica', 30, 'bold',), pady="-5", padx="5")
    l2.place(x=0, y=100)
    l2.config(bg=prim_color, fg="white")
    Button(Calculator, text='C', width=7, height=3, font=(20), bg=sec_color, bd=4, fg=prim_color,
           command=clear, activebackground="black", activeforeground="white").place(x=0, y=150)
    Button(Calculator, text='/', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('/'), activebackground="black", activeforeground="white").place(x=100, y=150)
    Button(Calculator, text='%', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('%'), activebackground="black", activeforeground="white").place(x=200, y=150)
    Button(Calculator, text='^', width=7, height=3, font=(20), bg='#282C35', bd=1, fg='white',
           command=lambda: show('**'), activebackground="black", activeforeground="white").place(x=300, y=150)
    Button(Calculator, text='7', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('7'), activebackground="black", activeforeground="white").place(x=0, y=250)
    Button(Calculator, text='8', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('8'), activebackground="black", activeforeground="white").place(x=100, y=250)
    Button(Calculator, text='9', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('9'), activebackground="black", activeforeground="white").place(x=200, y=250)
    Button(Calculator, text='-', width=7, height=3, font=(20), bg='#282C35', bd=1, fg='white',
           command=lambda: show('-'), activebackground="black", activeforeground="white").place(x=300, y=250)
    Button(Calculator, text='4', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('4'), activebackground="black", activeforeground="white").place(x=0, y=350)
    Button(Calculator, text='5', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('5'), activebackground="black", activeforeground="white").place(x=100, y=350)
    Button(Calculator, text='6', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('6'), activebackground="black", activeforeground="white").place(x=200, y=350)
    Button(Calculator, text='+', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('+'), activebackground="black", activeforeground="white").place(x=300, y=350)
    Button(Calculator, text='1', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('1'), activebackground="black", activeforeground="white").place(x=0, y=450)
    Button(Calculator, text='2', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('2'), activebackground="black", activeforeground="white").place(x=100, y=450)
    Button(Calculator, text='3', width=7, height=3, font=(20), bg='#282C35', bd=4, fg='white',
           command=lambda: show('3'), activebackground="black", activeforeground="white").place(x=200, y=450)
    Button(Calculator, text='=', width=7, height=8, font=(20), bg=sec_color, bd=4, fg=prim_color,
           command=cal, activebackground="black", activeforeground="white").place(x=300, y=453)
    Button(Calculator, text='0', width=18, height=3, font=(20), bg='#282C35', fg='white', command=lambda: show(
        '0'), activebackground="black", activeforeground="white").place(x=1, y=550)
    Button(Calculator, text='.', width=7, height=3, font=(20), bg='#282C35', fg='white', command=lambda: show(
        '.'), activebackground="black", activeforeground="white").place(x=200, y=550)
    
    
# all box labels
amt_label = tk.Label(Office, text="Amount: ", font=(
    prim_font, 18, "bold"), bg=prim_color, fg=sec_color).place(x=label_x, y=150)
from_label = tk.Label(Office, text="From : ", font=(
    prim_font, 18, "bold"), bg=prim_color, fg=sec_color).place(x=label_x, y=250)
to_label = tk.Label(Office, text="To : ", font=(
    prim_font, 18, "bold"), bg=prim_color, fg=sec_color).place(x=label_x, y=350)
convertedAmt_label = tk.Label(Office, text="Converted  ", font=(
    prim_font, 18, "bold"), bg=prim_color, fg=sec_color).place(x=label_x, y=550)
convertedAmt_label = tk.Label(Office, text="Amount: ", font=(
    prim_font, 18, "bold"), bg=prim_color, fg=sec_color).place(x=label_x+10, y=590)


conv_amt = tk.DoubleVar()
conv_amt.set(0.0)

newAmt = tk.Label(
    Office,
    textvariable=conv_amt,
    font=(prim_font, 18),
    fg=sec_color,
    bg=prim_color,
    borderwidth=0.5,
    # insertbackground= sec_color
).place(x=btn_x, y=550)


# input boxes
original_amt = tk.Entry(
    Office,
    font=(prim_font, 18),
    fg=sec_color,
    bg=prim_color,
    borderwidth=0.5,
    insertbackground=sec_color
)
original_amt.place(x=btn_x, y=150)


# Drop down button 1
from_btn_var = tk.StringVar()
from_btn_var.set("Select")
from_btn = tk.OptionMenu(
    Office, from_btn_var, "                        INR                          ")


from_btn.config(
    fg=sec_color,
    bg=prim_color,
    activeforeground=prim_color,
    activebackground=sec_color,
    border=0,
    highlightbackground=sec_color,
    highlightthickness=0.5,
    indicatoron=0,
    font=(prim_font, 13),
    width=22
)
from_btn["menu"].config(
    fg=sec_color,
    bg=prim_color,
    font=(prim_font, 12),
    activeborder=0,
    border=0,

)
from_btn.place(x=btn_x, y=260)


# Drop down button 2

to_btn_var = tk.StringVar()
to_btn_var.set("Select")
to_btn = tk.OptionMenu(Office, to_btn_var, *currency_rate)
to_btn.config(
    fg=sec_color,
    bg=prim_color,
    activeforeground=prim_color,
    activebackground=sec_color,
    border=0,
    highlightbackground=sec_color,
    highlightthickness=0.5,
    indicatoron=0,
    font=(prim_font, 13),
    width=22
)
to_btn["menu"].config(
    fg=sec_color,
    bg=prim_color,
    font=(prim_font, 12),
    activeborder=0,
    border=0
)
to_btn.place(x=btn_x, y=360)


# Convert ,Clear All and Calculator buttons

convert_btn = tk.Button(
    Office,
    text="Convert",
    command=update_label,
    font=(prim_font, 18),
    fg=sec_color,
    bg=prim_color,
    width=10,
    height=1,
    activebackground=sec_color,
    activeforeground=prim_color
)
convert_btn.place(x=clickBtn_x, y=150)

clear_btn = Button(
    Office,
    text="Clear All",
    command=clear_input,
    font=(prim_font, 18),
    fg=sec_color,
    bg=prim_color,
    width=10,
    height=1,
    activebackground=sec_color,
    activeforeground=prim_color,
).place(x=clickBtn_x, y=250)

#creating calculator button to open on new window

calc_btn = Button(
    Office,
    text="Calculator",
    command=open_cal,
    font=(prim_font, 18),
    fg=sec_color,
    bg=prim_color,
    width=10,
    height=1,
    activebackground=sec_color,
    activeforeground=prim_color,
).place(x=clickBtn_x, y=350)

tk.mainloop()
