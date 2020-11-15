from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile
import os
def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    Textarea.delete(1.0,END)



def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetype=[("All Files","*.*"),("Text Documents","*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.pth.basename(file) + " - Notepad")
        Textarea.delete(1.0,END)
        f=open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close
def saveFile():
    global file
    if file==None:
        file= asksaveasfile(initialfile="Untitled.txt",defaultextension=".txt",filetype=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")
        print("File Saved")
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def quitApp():
    root.destroy()
def about():
    showinfo("Notepad","Notepad by KT")

root=Tk()
root.geometry("644x788")
root.title("Notepad")
root.wm_iconbitmap("notepad.jfif")

Textarea = Text(root,font="lucida 15")
file= None
Textarea.pack(expand=True,fill=BOTH)

menubar = Menu(root)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label='Open',command = openFile)
filemenu.add_command(label="Save",command =saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitApp)
menubar.add_cascade(label="File",menu=filemenu)


editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
menubar.add_cascade(label="Edit",menu = editmenu)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)
root.config(menu=menubar)

Scroll = Scrollbar(Textarea)
Scroll.pack(side=RIGHT,fill=Y)
Textarea.config(yscrollcommand=Scroll.set)
Scroll.config(command=Textarea.yview)

root.mainloop()