from tkinter import *

root = Tk()
root.title("Team DevDuo/DebuggingDuo/Dev-N-Debug")
root.iconbitmap("moneyIcon.ico")

button_expenseTab = Button(root, text = "Expense Log", fg = "#000000", bg = "#00ff00")
button_CurrencyTab = Button(root, text = "Currency", bg = "#000000", fg = "#00ff00")

button_expenseTab.grid(row = 0, column=0)
button_CurrencyTab.grid(row = 0, column=1)

root.mainloop()