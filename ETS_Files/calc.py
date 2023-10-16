from tkinter import *
from tkinter import messagebox 
win = Tk()
win.config(height=650,width=390)
win.resizable(False,False)
win.configure(bg="black")
win.title("Calculator")
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
    
    
l2=Label(win,text='',font=('Helvetica', 20,'bold'))
l2.place(x=0,y=100)
Button(win,text='C',width=7,height=3,font=(20),bg=sec_color,bd=4,fg=prim_color,command=clear).place(x=0,y=150)
Button(win,text='/',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('/'), activebackground="black").place(x=100,y=150)
Button(win,text='%',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('%'), activebackground="black").place(x=200,y=150)
Button(win,text='',width=7,height=3,font=(20),bg='#282C35',bd=1,fg='white',command=lambda:show('')).place(x=300,y=150)

Button(win,text='7',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('7')).place(x=0,y=250)
Button(win,text='8',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('8')).place(x=100,y=250)
Button(win,text='9',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('9')).place(x=200,y=250)
Button(win,text='-',width=7,height=3,font=(20),bg='#282C35',bd=1,fg='white',command=lambda:show('-')).place(x=300,y=250)

Button(win,text='4',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('4')).place(x=0,y=350)
Button(win,text='5',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('5')).place(x=100,y=350)
Button(win,text='6',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('6')).place(x=200,y=350)
Button(win,text='+',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('+')).place(x=300,y=350)

Button(win,text='1',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('1')).place(x=0,y=450)
Button(win,text='2',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('2')).place(x=100,y=450)
Button(win,text='3',width=7,height=3,font=(20),bg='#282C35',bd=4,fg='white',command=lambda:show('3')).place(x=200,y=450)
Button(win,text='=',width=7,height=8,font=(20),bg=sec_color,bd=4,fg=prim_color,command=cal).place(x=300,y=453)

Button(win,text='0',width=18,height=3,font=(20),bg='#282C35',fg='white',command=lambda:show('0')).place(x=1,y=550)
Button(win,text='.',width=7,height=3,font=(20),bg='#282C35',fg='white',command=lambda:show('.')).place(x=200,y=550)

win.mainloop()