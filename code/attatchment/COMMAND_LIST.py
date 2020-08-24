# coding:UTF-8

from tkinter import*
from platform import system as pfsystem

command=['about','tkversion_and_system',]
def run_command():
    if a.get()==command[0]:
        print('Tktext1.0')
    elif a.get()==command[1]:
        print(tkversion)
        print(pfsystem())
    a.delete(0,END)

root=Tk()
root.title('Command List')
Label(root,text='Command List of Tktext(c)zhihongwang250.\n(c)zhihongwang250.保留一切权利。')\
    .grid(row=0,column=1)
Label(root,text='Command>>>').grid(row=1,column=0)
a=Entry(root)
a.grid(row=1,column=1)
Button(root,text='OK',command=run_command).grid(row=1,column=2)
root.mainloop()