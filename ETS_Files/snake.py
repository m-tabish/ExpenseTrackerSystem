import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkfont

# Create a Tkinter root window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("900x700")
root.config(bg="black")

# Define default font style
prim_font = tkfont.nametofont("TkDefaultFont")
prim_font.configure(family="Times New Roman", size=14)

# Global variables
prim_color = "black"
sec_color = "green"

# Create a Treeview widget for the table
table = ttk.Treeview(root, columns=("Date", "Spent On", "Amount", "Balance"), height=7)
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

# Configure Treeview style
style = ttk.Style()
style.configure("Treeview", background="black", fieldbackground=prim_color, foreground="white")

# Functions
data = []

def add():
    date_input = date_entry.get()
    spent_input = spent_entry.get()
    amount_input = amount_entry.get()

    if not date_input or not spent_input or not amount_input:
        messagebox.showerror("Error", "Please enter all the values")
        return

    data.append([date_input, spent_input, amount_input])

    for item in data:
        table.insert("", "end", values=item)

    data.clear()

def clear():
    date_entry.delete(0, "end")
    spent_entry.delete(0, "end")
    amount_entry.delete(0, "end")

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
style.configure("Treeview", rowheight=row_height, bg="black")
table.pack()

# Create a label and Input Fields
date_label = tk.Label(root, text="Date:", font=("Arial", 18), fg="white", bg=prim_color)
date_label.place(y=340, x=60)

date_entry = tk.Entry(root, font=("Arial", 18), fg="white", bg=prim_color, borderwidth=0.5, insertbackground="#00ff00")
date_entry.config(width=14)
date_entry.place(y=340, x=200)

spent_label = tk.Label(root, text="Spent On: ", font=("Arial", 18), fg="white", bg=prim_color)
spent_label.place(y=390, x=60)

spent_entry = tk.Entry(root, font=("Arial", 18), fg="white", bg=prim_color, borderwidth=0.5, insertbackground="#00ff00")
spent_entry.config(width=14)
spent_entry.place(y=3