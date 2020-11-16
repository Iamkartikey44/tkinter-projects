from tkinter import *

def click(event):
    text=event.widget.cget("text")
    print(text)
    if text=='=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value='ERROR'
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() +text)
        screen.update()

root = Tk()
root.geometry("544x366")
root.title("Calculator")
root.wm_iconbitmap("Martz90-Circle-Calculator.ico")
scvalue = StringVar()
input_frame = Frame(root,width=366,height=50,bd=0,highlightbackground='black',highlightcolor='black',highlightthickness=2)
input_frame.pack(side=TOP)
scvalue.set("")
screen = Entry(input_frame,textvar=scvalue,font= " arial 18 bold",width=50,bg='#eee',bd=0,justify=RIGHT)
screen.grid(row=0,column=0)
screen.pack(ipady=10)
f1 = Frame(root,width=312,height=272.5,bg='grey')
nine = Button(f1,text="9",fg='black',width=10,height=3,bd=0,bg='#fff',cursor= 'hand2')
nine.pack(side=LEFT,padx=1,pady=1)
nine.bind("<Button-1>",click)

eight = Button(f1,text="8",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
eight.pack(side=LEFT,padx=1,pady=1)
eight.bind("<Button-1>",click)

seven = Button(f1,text="7",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
seven.pack(side=LEFT,padx=1,pady=1)
seven.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,width=312,height=272.5,bg='grey')
six = Button(f1,text="6",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
six.pack(side=LEFT,padx=1,pady=1)
six.bind("<Button-1>",click)

five = Button(f1,text="5",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
five.pack(side=LEFT,padx=1,pady=1)
five.bind("<Button-1>",click)

four = Button(f1,text="4",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
four.pack(side=LEFT,padx=1,pady=1)
four.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,width=312,height=272.5,bg='grey')
three = Button(f1,text="3",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
three.pack(side=LEFT,padx=1,pady=1)
three.bind("<Button-1>",click)

two = Button(f1,text="2",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
two.pack(side=LEFT,padx=1,pady=1)
two.bind("<Button-1>",click)

one = Button(f1,text="1",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
one.pack(side=LEFT,padx=1,pady=1)
one.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,width=312,height=272.5,bg='grey')
zero = Button(f1,text="0",fg='black',width=10,height=3,bd=0,bg='#fff',cursor='hand2')
zero.pack(side=LEFT,padx=1,pady=1)
zero.bind("<Button-1>",click)

subtract = Button(f1,text="-",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
subtract.pack(side=LEFT,padx=1,pady=1)
subtract.bind("<Button-1>",click)

add = Button(f1,text="+",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
add.pack(side=LEFT,padx=1,pady=1)
add.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,width=312,height=272.5,bg='grey')
divide = Button(f1,text="/",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
divide.pack(side=LEFT,padx=1,pady=1)
divide.bind("<Button-1>",click)

percentage = Button(f1,text="%",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
percentage.pack(side=LEFT,padx=1,pady=1)
percentage.bind("<Button-1>",click)

multiply = Button(f1,text="*",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
multiply.pack(side=LEFT,padx=1,pady=1)
multiply.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root,width=312,height=272.5,bg='grey')

point = Button(f1,text=".",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
point.pack(side=LEFT,padx=1,pady=1)
point.bind("<Button-1>",click)

clear = Button(f1,text="C",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
clear.pack(side=LEFT,padx=1,pady=1)
clear.bind("<Button-1>",click)

equal = Button(f1,text="=",fg='black',width=10,height=3,bd=0,bg='#eee',cursor='hand2')
equal.pack(side=LEFT,padx=1,pady=1)
equal.bind("<Button-1>",click)
f1.pack()

root.mainloop()

