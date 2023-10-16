import tkinter as tk
from tkinter import ttk

def change_tab(event):
    current_tab = notebook.index(notebook.select())
    if current_tab == 0:
        tab1_frame.configure(bg="lightblue")
        tab2_frame.configure(bg="white")
    elif current_tab == 1:
        tab1_frame.configure(bg="white")
        tab2_frame.configure(bg="lightblue")

root = tk.Tk()
root.title("Custom Tab Background Color")
root.geometry("400x300")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

tab1_frame = tk.Frame(notebook, bg="lightblue")
tab2_frame = tk.Frame(notebook, bg="white")

notebook.add(tab1_frame, text="Tab 1")
notebook.add(tab2_frame, text="Tab 2")

notebook.bind("<<NotebookTabChanged>>", change_tab)

root.mainloop()
