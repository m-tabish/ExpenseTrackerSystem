import tkinter as tk
from tkinter import ttk
from tkmacosx import Button
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials, firestore
# Fetching Firestore credentials and initializing the app
cred = credentials.Certificate("serviceAccountKey.json")  # Update with your Firebase service account key
firebase_admin.initialize_app(cred)
db = firestore.client()
counter = 0
def addExpense(payload):
    try:
        doc_ref = db.collection("expenses").add(payload)
        return {"status": 1, "resp": doc_ref}
    except Exception as e:
        print("Error adding document: ", str(e))
        return {"status": 1, "message": e}
# Global variables for pagination
last_expense = None
expense_counter = 1  # Counter for serial number
# Create a Tkinter root window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("720x500")
root.config(bg="black")
root.resizable(False, False)
# Data Initialize for the Treeview
data = []
# Function to retrieve next 10 expenses and update the Tkinter Treeview widget
def load_more_expenses():
    global last_expense, expense_counter, counter
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    loading_window.geometry("200x100")
    loading_label = tk.Label(loading_window, text="Fetching Expense...", font=("Arial", 12))
    loading_label.pack(pady=20)
    len_expenses = 0
    root.update()
    # Check if last_expense is None, set it to an empty string in that case
    if last_expense is None:
        last_expense = ""

    expenses = db.collection("expenses").order_by("date").start_after(last_expense).limit(10).stream()
    for expense in expenses:
        len_expenses += 1
        counter += 1

        data.append({
            "date": expense.get('date'),
            "spent_on": expense.get('spent_on'),
            "amount": expense.get('amount'),
            "key": expense.id
        })
        update_treeview()
        last_expense = expense
        expense_counter += 1

    # Check if there are more expenses, if not, hide the Load More button
    if len_expenses == 0:
        load_More.destroy()
        
        messagebox.showinfo("Alert","No more expenses to load.")
    loading_window.destroy()
# Function to fetch the initial 10 expenses and update the Tkinter Treeview widget
def show_initial_expenses():
    global last_expense, expense_counter, counter
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    loading_window.geometry("200x100")
    loading_label = tk.Label(loading_window, text="Fetching Expense...", font=("Arial", 12))
    loading_label.pack(pady=20)
    len_expenses = 0
    root.update()
    expenses = db.collection("expenses").order_by("date").limit(10).stream()
    for expense in expenses:
        counter += 1
        data.append({
            "date": expense.get('date'),
            "spent_on": expense.get('spent_on'),
            "amount": expense.get('amount'),
            "key": expense.id
        })
        last_expense = expense  # Update last_expense here
        expense_counter += 1
    update_treeview()
    loading_window.destroy()
# Function to update the Tkinter Treeview with the data
def update_treeview():
    # Clear existing items in the Treeview
    if not data:
        # If there are no expenses, add a row with a message
        table.insert("", "end", values=("No Expense Found", "", "", "", ""))
        return
    for item in table.get_children():
        table.delete(item)

# Insert data into the Treeview with sequential serial number
    for i, item in enumerate(data, start=1):
        table.insert("", "end", values=(i, item["date"], item["spent_on"], item["amount"], item["key"]))
# Create a Treeview widget for the table
table = ttk.Treeview(root, columns=("No", "Date", "Spent On", "Amount", "Balance"), height=7)
table.heading("#1", text="No")
table.heading("#2", text="Date")
table.heading("#3", text="Spent On")
table.heading("#4", text="Amount")

def add_expense():
     # Get data from input fields
    date_value = date_entry.get()
    spent_on_value = spent_entry.get()
    amount_value = amount_entry.get()
    # Validate if all fields are filled
    if not (date_value and spent_on_value and amount_value):
        # You can show an error message or handle this case in another way
        messagebox.showerror("Error", "Please fill all the fields")
        return

    global counter
    loading_window = tk.Toplevel(root)
    loading_window.title("Loading...")
    loading_window.geometry("200x100")
    loading_label = tk.Label(loading_window, text="Adding Expense...", font=("Arial", 12))
    loading_label.pack(pady=20)

    # Update the main window during the loading process
    root.update()
   


    # Create a payload tuple
    expense_payload = {
        "date": date_value,
        "spent_on": spent_on_value,
        "amount": amount_value
    }

    print(expense_payload)
    # Call the addExpense function with the payload
    resp = addExpense(expense_payload)
    # Close the loading window after the operation completes
    loading_window.destroy()

    if resp.get("status") == 1:
        print("Expense added successfully")
        timestamp, doc_ref = resp.get("resp")
        expense_payload["key"] = doc_ref.id

        data.append(expense_payload)
        counter += 1

        update_treeview()

    else:
        print(f"Error adding expense: {resp.get('message')}")
    # Clear input fields after adding an expense
    date_entry.delete(0, tk.END)
    spent_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
# Add an event to the Treeview to capture double-clicks
table.bind("<Double-1>", lambda event: on_treeview_double_click(event))

# Function to handle double-click event on the Treeview
def on_treeview_double_click(event):
    item = table.selection()[0]  # Get the selected item
    item_values = table.item(item, "values")  # Get the values of the selected item
    print(item_values)
    # Open anew window for updating the expense
    update_window = tk.Toplevel(root)
    update_window.title("Update Expense")
    update_window.geometry("300x200")

    # Create labels and entry widgets for updating fields
    date_label = tk.Label(update_window, text="Date", font=("Arial", 12))
    date_label.grid(row=0, column=0, padx=10, pady=10)
    date_entry = tk.Entry(update_window, font=("Arial", 12))
    date_entry.grid(row=0, column=1, padx=10, pady=10)
    date_entry.insert(0, item_values[1])

    spent_on_label = tk.Label(update_window, text="Spent On", font=("Arial", 12))
    spent_on_label.grid(row=1, column=0, padx=10, pady=10)
    spent_on_entry = tk.Entry(update_window, font=("Arial", 12))
    spent_on_entry.grid(row=1, column=1, padx=10, pady=10)
    spent_on_entry.insert(0, item_values[2])

    amount_label = tk.Label(update_window, text="Amount", font=("Arial", 12))
    amount_label.grid(row=2, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(update_window, font=("Arial", 12))
    amount_entry.grid(row=2, column=1, padx=10, pady=10)
    amount_entry.insert(0, item_values[3])

    # Function to update the expense
    def update_expense():
        new_date = date_entry.get()
        new_spent_on = spent_on_entry.get()
        new_amount = amount_entry.get()

        # Validate if all fields are filled
        if not (new_date and new_spent_on and new_amount):
            messagebox.showerror("Error", "Please fill all the fields")
            return

        # Update the data in the data list
        updated_data = {
            "date": new_date,
            "spent_on": new_spent_on,
            "amount": new_amount,
            "key": item_values[4]  # The key of the expense
        }

        try:
            # Attempt to update the expense in Firestore
            db.collection("expenses").document(item_values[4]).update({
                "date": new_date,
                "spent_on": new_spent_on,
                "amount": new_amount
            })
            print("Updated expense")
            # If the update in Firestore is successful, update the data in the data list
            data[table.index(item)] = updated_data
            update_treeview()  # Refresh the Treeview widget
            # Close the update window
            update_window.destroy()
        except Exception as e:
            # If an error occurs during the Firestore update, show an alert message
            messagebox.showerror("Error", f"Failed to update expense: {str(e)}")
    

    # Button to trigger the update
    update_button = tk.Button(update_window, text="Update", command=update_expense)
    update_button.grid(row=3, column=0, columnspan=2, pady=10)

# function for exiting 

def onExit():
    root.destroy()

# Calculate the width of each column to make them evenly spaced
total_columns = 3
table_width = 720
column_width = table_width // total_columns
for i in range(total_columns):
    table.column(i, width=column_width, anchor="center")

# Hide the first column
table.column("#0", width=0, stretch=tk.NO)

style = ttk.Style()
style.configure("Treeview",
                background="black",
                fieldbackground="black",
                foreground="white",
                )

# Clear fun
def clear_input_fields():
    date_entry.delete(0, tk.END)
    spent_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

for item in data:
    table.insert("", "end", values=(expense_counter, item["date"], item["spent_on"], item["amount"]))

# Calculate the row height (in pixels)
row_height = 40

# Create a custom style to adjust row height
style = ttk.Style()
style.configure("Treeview", rowheight=row_height)
table.pack()

line_frame = tk.Frame(root, width=720, height=2, bg="#00ff00")
line_frame.place(y=320, x=0)

# Create a label and Input Fields
date_label = tk.Label(root, text="Date", font=("Arial", 18), fg="white", bg="black")
date_label.place(y=340, x=10)

date_entry = tk.Entry(root, font=("Arial", 18), fg="white", bg="black", borderwidth=0.5)
date_entry.config(width=14)
date_entry.place(y=340, x=100)

spent_label = tk.Label(root, text="Spent On ", font=("Arial", 18), fg="white", bg="black")
spent_label.place(y=390, x=10)

spent_entry = tk.Entry(root, font=("Arial", 18), fg="white", bg="black", borderwidth=0.5)
spent_entry.config(width=14)
spent_entry.place(y=390, x=100)

amount_label = tk.Label(root, text="Amount ", font=("Arial", 18), fg="white", bg="black")
amount_label.place(y=440, x=10)

amount_entry = tk.Entry(root, font=("Arial", 18), fg="white", bg="black", borderwidth=0.5)
amount_entry.config(width=14)
amount_entry.place(y=440, x=100)

# Buttons
clean = Button(root, text="Clear", bg="black", fg="green", font=("Arial", 18), command=clear_input_fields)
clean.place(y=360, x=280)

add = Button(root, text="Add", bg="black", fg="green", font=("Arial", 18), command=add_expense)
add.place(y=410, x=280)
#message for no load more expenses
load_more_msg=tk.Label(root, text="No More Expense", bg="black", font=("Arial", 15),fg="green")
load_more_msg.place(y=365, x=410)
load_More = Button(root, text="Load More", bg="black", fg="green", font=("Arial", 18), command=load_more_expenses)
load_More.place(y=360, x=410)


delete = Button(root, text="Delete", bg="black", fg="green", font=("Arial", 18))
delete.place(y=360, x=590)

exit_button = Button(root, text="Exit", bg="black", fg="green", font=("Arial", 18),command=onExit)
exit_button.place(y=410, x=410)

# Start the Tkinter main loop
# Display initial 10 expenses
show_initial_expenses()

root.mainloop()
