import tkinter as tk
from tkinter import ttk
# from tkmacosx import Button
from tkinter import Button
import tkinter.font as tkfont

# Create a Tkinter root window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("1000x840")
root.config(bg="black")
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
                background=prim_color, 
                fieldbackground=prim_color, 
                foreground="white"
                
                )


# Add some dummy data to the Treeview
data = [
    
    ("2023-10-02", "Utilities", "$100.00", "$400.00"),
    ("2023-10-03", "Dining Out", "$30.00", "$370.00"),
    ("2023-10-04", "Entertainment", "$20.00", "$350.00"),
    ("2023-10-04", "Entertainment", "$20.00", "$350.00"),
    ("2023-10-04", "Entertainment", "$20.00", "$350.00"),
    ("2023-10-04", "Entertainment", "$20.00", "$350.00"),
    ("2023-10-01", "Groceries", "$50.00", "$500.00"),
    ("2023-10-02", "Utilities", "$100.00", "$400.00"),
    ("2023-10-03", "Dining Out", "$30.00", "$370.00"),
    ("2023-10-04", "Entertainment", "$20.00", "$350.00"),
    ("2023-10-04", "Entertainment", "$20.00", "$350.00"),
]

for item in data:
    table.insert("", "end", values=item)
    
# Calculate the row height (in pixels)
row_height = 40

# Create a custom style to adjust row height
style = ttk.Style()
style.configure("Treeview", rowheight=row_height)
table.pack()

line_frame = tk.Frame(root, width=720, height=2, bg="#00ff00")
line_frame.place(y=320,x=0)

# Create a label and Input Fields
date_label = tk.Label(root, text="Date",font=("Airal",18),fg="white",bg=prim_color)
date_label.place(y=340,x=10)

date_entry = tk.Entry(root,font=("Airal",18),fg="white",bg=prim_color,borderwidth=0.5)
date_entry.config(width=14)
date_entry.place(y=340,x=100)

spent_label = tk.Label(root, text="Spent On ",font=("Airal",18),fg="white",bg=prim_color)
spent_label.place(y=390,x=10)

spent_entry = tk.Entry(root,font=("Airal",18),fg="white",bg=prim_color,borderwidth=0.5)
spent_entry.config(width=14)
spent_entry.place(y=390,x=100)


amount_label = tk.Label(root, text="Amount ",font=("Airal",18),fg="white",bg=prim_color)
amount_label.place(y=440,x=10)

amount_entry = tk.Entry(root,font=("Airal",18),fg="white",bg=prim_color,borderwidth=0.5)
amount_entry.config(width=14)
amount_entry.place(y=440,x=100)


# Buttons
clean = Button(root, text="Clear", bg=prim_color, fg="green",font=("Airal",18))
clean.place(y=360,x=380)

add = Button(root, text="Add", bg=prim_color, fg="green",font=("Airal",18))

add.place(y=410,x=280)

total_amount = Button(root, text="Total Amount", bg=prim_color, fg="green",font=("Airal",18))
total_amount.place(y=360,x=410)

update = Button(root, text="      Update     ", bg=prim_color, fg="green",font=("Airal",18))
update.place(y=410,x=410)


delete = Button(root, text="Delete", bg=prim_color, fg="green",font=("Airal",18))
delete.place(y=360,x=590)

exit = Button(root, text="Exit", bg=prim_color, fg="green",font=("Airal",18))
exit.place(y=410,x=590)

# Start the Tkinter main loop
root.mainloop()