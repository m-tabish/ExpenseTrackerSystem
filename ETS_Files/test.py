import tkinter as tk
from tkinter import ttk
# from tkmacosx import Button
from tkinter import Button
import tkinter.font as tkfont

# Create a Tkinter root window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("900x700")
root.config(bg="black")
img = tk.PhotoImage(
    False, file="D:\ExpenseTrackerSystem\ETS_Files\PrismOfficeLogo.png")
root.iconphoto(False, img)
root.resizable(False, False)

#defining default font style 
prim_font = tkfont.nametofont("TkDefaultFont")
prim_font.configure(family="Times New Roman", size=14)


#global variables
global prim_color 
global sec_color 
prim_color = "black"
sec_color = "green"

# Create a Treeview widget for the table
table = ttk.Treeview(root, columns=("Date", "Spent On", "Amount", "Balance"),height=7)
table.heading("#1", text="Date")  
table.heading("#2", text="Spent On")
table.heading("#3", text="Amount")
table.heading("#4", text="Balance")


# Calculate the width of each column to make them evenly spaced
total_columns = 4  
table_width = 720  
column_width = table_width // total_columns  
for i in range(total_columns):
    table.column(i, width=column_width, anchor="center")

# Hide the first column
table.column("#0", width=0, stretch=tk.NO)

style = ttk.Style()
style.configure("Treeview",
                background="black", 
                fieldbackground=prim_color, 
                foreground="white"
                
                )

#functions 
global date_input
global spent_input 
global amount_input
data = []
def add():
    date_input = date_entry.get()
    spent_input = spent_entry.get()
    amount_input = amount_entry.get()
    if(date_input, spent_input, amount_input):
        data.append([date_input,spent_input,amount_input])
        
    for item in data:
        table.insert("", "end", values=item)
        data.clear()
    
def clear():
    date_input = date_entry.delete(0,"end")
    spent_input = spent_entry.delete(0,"end")
    amount_input = amount_entry.delete(0,'end')
    
def delete_record():
    selected_item = table.selection()
    if selected_item:
        table.delete(selected_item)

# Add some dummy data to the Treeview


for item in data:
    table.insert("", "end", values=item)
    
# Calculate the row height (in pixels)
row_height = 40

# Create a custom style to adjust row height
style = ttk.Style()
style.configure("Treeview", rowheight=row_height,bg="black")
table.pack()

line_frame = tk.Frame(root, width=720, height=2, bg="#00ff00")
line_frame.place(y=320,x=0)

# Create a label and Input Fields
date_label = tk.Label(root, text="Date",font=("Airal",18),fg="white",bg=prim_color)
date_label.place(y=340,x=10)

date_entry = tk.Entry(root,font=("Airal",18),fg="white",bg=prim_color,borderwidth=0.5, insertbackground="#00ff00")
date_entry.config(width=14)
date_entry.place(y=340,x=150)

spent_label = tk.Label(root, text="Spent On ",font=("Airal",18),fg="white",bg=prim_color)
spent_label.place(y=390,x=10)

spent_entry = tk.Entry(root,font=("Airal",18),fg="white",bg=prim_color,borderwidth=0.5, insertbackground="#00ff00")
spent_entry.config(width=14)
spent_entry.place(y=390,x=150)


amount_label = tk.Label(root, text="Amount ",font=("Airal",18),fg="white",bg=prim_color)
amount_label.place(y=440,x=10)

amount_entry = tk.Entry(root,font=("Airal",18),fg="white",bg=prim_color,borderwidth=0.5, insertbackground="#00ff00")
amount_entry.config(width=14)
amount_entry.place(y=440,x=150)


# Buttons
clean = Button(root, text=" Clear", command = clear,bg=prim_color, fg="green",font=("Airal",18))
clean.place(y=360,x=430)

add = Button(root, text="  Add ",command= add, bg=prim_color, fg="green",font=("Airal",18))

add.place(y=410,x=430)

total_amount = Button(root, text=" Total Amount ", bg=prim_color, fg="green",font=("Airal",18))
total_amount.place(y=360,x=520)

update = Button(root, text="      Update     ", bg=prim_color, fg="green",font=("Airal",18))
update.place(y=410,x=520)


delete = Button(root, text="  Delete  ",command = delete_record,  bg=prim_color, fg="green",font=("Airal",18))
delete.place(y=360,x=700)

exit = Button(root, text="    Exit    ",command = exit, bg=prim_color, fg="green",font=("Airal",18))
exit.place(y=410,x=700)

# Start the Tkinter main loop
root.mainloop()