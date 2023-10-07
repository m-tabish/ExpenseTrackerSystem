from tkinter import *
root = Tk()
root.title("Tabish")
root.geometry("1440x1000")


# main_frame = LabelFrame(root,text= "Currency Converter", padx= 50, pady=50)
title = Label(root, text = "Currency Converter", justify= CENTER,)
# amount = Label(root, text = "Amount")
# amt_input = Entry(root, width="100")
# btn_convert = Button(root, text = "Convert")

# main_frame.pack(padx=10, pady=10)
title.pack()
# amount.grid(row=1 , column = 0)
# amt_input.grid(row=1 , column = 1)
# btn_convert.grid(row=1 , column = 2)


root.mainloop()