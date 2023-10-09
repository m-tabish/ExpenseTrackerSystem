# # from tkinter import *

# # root = Tk()
# # root.title("Currency")
# # root.geometry("1440x900")

# # #Drop down menus

# # def show():
# #     myLabel = Label(root, text = clicked.get() ).pack()

# # clicked = StringVar()
# # clicked.set("Monday")


# # drop = OptionMenu(root, clicked, 'Monday', "Tuesday", "Wednesday")
# # drop.pack()


# # myButton = Button(root, text = "Show Selection", command = show).pack()

# # mainloop()





# ####################################################################
# # Python program to change menu background
# # color of Tkinter's Option Menu

# # # Import the library tkinter
# # from tkinter import *

# # # Create a GUI app
# # app = Tk()

# # # Give title to your GUI app
# # app.title("Vinayak App")

# # # Construct the label in your app
# # l1 = Label(app, text="Choose the week day here")

# # # Display the label l1
# # l1.grid()

# # # Construct the Options Menu widget in your app
# # text1 = StringVar()

# # # Set the value you wish to see by default
# # text1.set("Choose here")

# # # Create options from the Option Menu
# # w = OptionMenu(app, text1, "Sunday", "Monday", "Tuesday",
# # 			"Wednesday", "Thursday", "Friday", "Saturday")

# # # Se the background color of Options Menu to green
# # w.config(bg="GREEN", fg="WHITE")

# # # Set the background color of Displayed Options to Red
# # w["menu"].config(bg="RED")

# # # Display the Options Menu
# # w.grid(pady=20)

# # # Make the loop for displaying app
# # app.mainloop()



import tkinter as tk

root = tk.Tk()
# Create a function to update the label text with the input value
def update_label():
    input_text = entry.get()  # Get the text from the Entry widget
    label.config(text=f'You entered: {input_text}')  # Update the Label text

# Create the main application window
root.title("Input Box Example")

# Create an Entry widget for input
entry = tk.Entry(root)
entry.pack(padx=10, pady=10)

# Create a Button to trigger the update_label function
update_button = tk.Button(root, text="Update Label", command=update_label)
update_button.pack(pady=5)

# Create a Label widget to display the input value
label = tk.Label(root, text="")
label.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()



# import tkinter as tk

# def change_label_text():
#     if label_var.get() == "Hello":
#         label_var.set("Hello World")
#     else:
#         label_var.set("Hello")

# root = tk.Tk()
# root.title("Label Click Example")

# label_var = tk.StringVar()
# label_var.set("Hello")

# label = tk.Label(root, textvariable=label_var, font=("Helvetica", 24))
# label.pack(pady=20)

# button = tk.Button(root, text="Click me!", command=change_label_text)
# button.pack()
# root.mainloop()




# import tkinter as tk

# def get_entry_value():
#     entry_value = entry.get()
#     print("Entry Value:", entry_value)

# root = tk.Tk()
# root.title("Get Entry Value Example")

# entry = tk.Entry(root)
# entry.pack(pady=20)

# button = tk.Button(root, text="Get Entry Value", command=get_entry_value)
# button.pack()

# root.mainloop()