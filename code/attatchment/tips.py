# coding:UTF-8

from tkinter import*
from tkinter import Tk,Frame
from tkinter.ttk import Notebook

root=Tk()
root.title('小提示')
root.geometry('500x300')
note=Notebook(root)

f=Frame()
f2=Frame()
f3=Frame()

Label(f,text='在窗口上方有一个输入框，您可以输入您要的大小（如：华文楷体 20 bold）').pack()
Label(f,text='您如果只想改变大小，那就输入大小').pack()

Label(f2,text='您可以点击打开文件命令，打开您要的文件。您可以打开\nnotepad支持的所有文件后缀。').pack()

Label(f3,text='Command List是一个类似cmd的程序，您可以在这里输入命令。\n\
    目前有两个命令。分别是about，tkversion_and_system。')\
        .pack()

note.add(f,text='设置文字大小')
note.add(f2,text='如何打开文件')
note.add(f3,text='Command List')
note.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()