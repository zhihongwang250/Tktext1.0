# coding:UTF-8
# 创建文件时使用的编辑器：Visual Studio Code

from tkinter import messagebox,Tk,Text,Menu,BOTH,END,RIGHT,Y,Label,HORIZONTAL,X
from tkinter import Checkbutton,BooleanVar,TkVersion,DISABLED,NORMAL,INSERT
from tkinter import Entry,Scale,StringVar,Button,SEL,SEL_FIRST,SEL_LAST
from tkinter.font import Font
from tkinter.colorchooser import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Separator

import sys
from platform import system
import webbrowser as vb
import os

def run1():
    with open(filename,'r') as f:
        exec(f.read())

def pyshell():
    print('退出pyshell：输入exit')
    os.system('python')
    print('pyshell结束')

def newfile():
    text.delete("1.0",END)
    root.title("Tktext1:Untitled")

def exit_ask():
    askexit=messagebox.askyesno('提示','退出Tktext？')
    if askexit==True:
        sys.exit()
    else:
        return

def open_file():
    global filename
    global contennt
    filename=askopenfilename()
    if filename=='':
        return
    with open(filename,'r', encoding='UTF-8') as fileobj:
        contennt=fileobj.read()
        text.delete("1.0",END)
        text.insert(END,contennt)
        filename1=filename+'-Tktext文字'
        root.title(filename1)

def save_file():
    global filename
    textContent=text.get("1.0",END)
    filename=asksaveasfilename(defaultextension='.py')
    if filename=='':
        return
    with open(filename,'w', encoding='UTF-8') as output:
        output.write(textContent)
        root.title(filename)

def readonly():
    if asa.get()==True:
        text.config(state=DISABLED)
    else:
        text.config(state=NORMAL)

def show(event):
    tanchu.post(event.x_root,event.y_root)

def copy():
    try:
        text.event_generate("<<Copy>>")
    except TclError:
        print('无数据')

def cut():
    try:
        text.event_generate('<<Cut>>')
    except TclError:
        print('无数据')

def paste():
    try:
        text.event_generate("<<Paste>>")
    except TclError:
        print('无数据')

root=Tk()
root.title("Tktext1:Untitled")
root.geometry('1500x600')

text=ScrolledText(root,undo=True)
text.pack(fill=BOTH,expand=True)
root.protocol("WM_DELETE_WINDOW",exit_ask)

font1=Font(weight='normal')
text.configure(font=font1)

menubar=Menu(root)
file=Menu(menubar,tearoff=False)
file2=Menu(menubar,tearoff=False)
file3=Menu(menubar,tearoff=False)
file4=Menu(menubar,tearoff=False)
run=Menu(menubar,tearoff=False)

asa=BooleanVar(root)
asa.set(False)

tanchu=Menu(root,tearoff=0)
tanchu.add_command(label='复制',command=copy)
tanchu.add_command(label='剪切',command=cut)
tanchu.add_command(label='粘贴',command=paste)

root.bind("<Button-3>",show)
menubar.add_cascade(label='文件(F)',menu=file)
file.add_command(label='新建文档',command=newfile,accelerator='Ctrl+N')
file.add_command(label='打开文档',command=open_file,accelerator='Ctrl+O')
file.add_command(label='保存文档',command=save_file,accelerator='Ctrl+S')
root.config(menu=menubar)
menubar.add_cascade(label='设置(S)',menu=file2)
file2.add_checkbutton(label='只读',command=readonly,variable=asa)
file2.add_cascade(label='运行程序',menu=run)
run.add_command(label='打开shell',command=pyshell)
run.add_command(label='运行',command=run)
root.config(menu=menubar)
root.config(menu=menubar)

root.mainloop()