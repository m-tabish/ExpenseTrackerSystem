import tkinter as tk
from tkinter import ttk
# from tkmacosx import Button
from tkinter import Button
from PIL import ImageTk, Image
from tkinter import messagebox
win = tk.Tk()
win.config(height=650,width=390)
win.resizable(False,False)
win.configure(bg="black")
win.title("Calculator")
win.iconphoto(False ,tk.PhotoImage(file= "D:\ExpenseTrackerSystem\ETS_Files\calculator.png"))
#global variables

global prim_font
global prim_color
global sec_color
global label_x
global btn_x 
global clickBtn_x
prim_font = "Poppins"
prim_color = "black"
sec_color = "#00ff00"


expression = ''

def show(val):
    global expression
    expression+=val
    l2.config(text=expression)
def clear():
    global expression
    expression = ''
    l2.config(text=expression)
def cal():
    result = ''
    global expression
    if expression != '' :
        try:
            result=str(eval(expression))
            
            expression = result
        except:
            messagebox.showwarning('Invalid','Invalid Operators and number use -_-')
            result='error'
                
            expression = result
    l2.config(text=expression)
    

    
l2=tk.Label(win,text='',font=('Helvetica', 30,'bold',),pady="-5", padx="5")
l2.place(x=0,y=100)
l2.config(bg = prim_color, fg="white")
Button(win,text='C',width=7,height=3,font=(20),bg=sec_color,bd=4,fg=prim_color,command=clear, activebackground="black", activeforeground="white").place(x=0,y=150)
Button(win,text='/',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('/'), activebackground="black", activeforeground="white").place(x=100,y=150)
Button(win,text='%',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('%'), activebackground="black", activeforeground="white").place(x=200,y=150)
Button(win,text='^',width=7,height=3,font=(20),bg='#282C35',bd=1,fg='white',command=lambda:show('**'), activebackground="black", activeforeground="white").place(x=300,y=150)

Button(win,text='7',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('7'), activebackground="black", activeforeground="white").place(x=0,y=250)
Button(win,text='8',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('8'), activebackground="black", activeforeground="white").place(x=100,y=250)
Button(win,text='9',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('9'), activebackground="black", activeforeground="white").place(x=200,y=250)
Button(win,text='-',width=7,height=3,font=(20),bg='#282C35',bd=1,fg='white',command=lambda:show('-'), activebackground="black", activeforeground="white").place(x=300,y=250)

Button(win,text='4',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('4'), activebackground="black", activeforeground="white").place(x=0,y=350)
Button(win,text='5',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('5'), activebackground="black", activeforeground="white").place(x=100,y=350)
Button(win,text='6',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('6'), activebackground="black", activeforeground="white").place(x=200,y=350)
Button(win,text='+',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('+'), activebackground="black", activeforeground="white").place(x=300,y=350)

Button(win,text='1',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('1'), activebackground="black", activeforeground="white").place(x=0,y=450)
Button(win,text='2',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('2'), activebackground="black", activeforeground="white").place(x=100,y=450)
Button(win,text='3',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('3'), activebackground="black", activeforeground="white").place(x=200,y=450)
Button(win,text='=',width=7,height=8,font=(20),bg=sec_color,bd=4,fg=prim_color,command=cal, activebackground="black", activeforeground="white").place(x=300,y=453)

Button(win,text='0',width=18,height=3,font=(20),bg='#282C35',fg='white',command=lambda:show('0'), activebackground="black", activeforeground="white").place(x=1,y=550)
Button(win,text='.',width=7,height=3,font=(20),bg='#282C35',fg='white',command=lambda:show('.'), activebackground="black", activeforeground="white").place(x=200,y=550)

win.mainloop()