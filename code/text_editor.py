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
from tkinter.ttk import Separator,Button

import sys
from platform import system
import webbrowser as vb

def choosecolor():
    mycolor=askcolor()
    print(type(mycolor),mycolor)
    text.config(fg=mycolor[1])

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
    filename=asksaveasfilename(defaultextension='.txt')
    if filename=='':
        return
    with open(filename,'w', encoding='UTF-8') as output:
        output.write(textContent)
        root.title(filename)
    
def about():
    about=Tk()
    about.title("关于Tktext")
    Label(about,text='Tktext：使用tkinter制作的文字处理系统\n版权所有(c)zhihongwang250.').pack()
    Separator(about,orient=HORIZONTAL).pack(fill=X,pady=10)
    Label(about,text='未经许可，不得抄袭本作品中的任何部分！').pack()
    Separator(about,orient=HORIZONTAL).pack(fill=X,pady=10)
    Label(about,text='TkVersion:{}'.format(TkVersion)).pack()
    Label(about,text='System:{}'.format(system())).pack()
    Label(about,text='Python Version:{}'.format(sys.version[:6])).pack()
    Button(about,text='确定',command=about.destroy).pack()
    about.mainloop()

def readonly():
    if asa.get()==True:
        text.config(state=DISABLED)
    else:
        text.config(state=NORMAL)

def open_help():
    helpfl=Tk()
    helpfl.title('帮助')
    text1=Text(helpfl,undo=True)
    text1.pack(fill=Y,expand=True)
    text1.insert(INSERT, '请到官网查看相关文档。\n这里不提供文档。')
    text1.tag_add('link', 1.3,1.4)
    text1.tag_config('link', foreground='blue', underline=True)
    def show_arrow_cursor(event):
        text.config(cursor='arrow')
    def show_xterm_cursor(event):
        text.config(cursor='xterm')
    def click(event):
        vb.open('https://zhihongwang250.github.io/tktext10_webside/')
    text1.tag_bind('link', '<Enter>', show_arrow_cursor)  #<Enter>鼠标进入
    text1.tag_bind('link', '<Leave>', show_xterm_cursor)  #<Enter>鼠标离开
    text1.tag_bind('link', '<Button-1>', click)  #<Enter>鼠标点击
    text1.config(state=DISABLED)
    helpfl.mainloop()

def jiacu():
    if asa1.get():
        font1=Font(weight='bold')
        text.configure(font=font1)
    else:
        font1=Font(weight='normal')
        text.configure(font=font1)

def ok():
    try:
        f=Font(family=entry1.get(),size=entry2.get())
        text.configure(font=f)
    except NameError:
        messagebox.showinfo('提示','您输入的字体不存在')
        return

def show(event):
    tanchu.post(event.x_root,event.y_root)

def Tksearch():
    def searchbox():
        text.tag_remove('found','1.0',END)
        start='1.0'
        key=entry3.get()

        if (len(key.strip())==0):
            return
        while True:
            pos=text.search(key,start,END)
            if (pos==''):
                break
            text.tag_add('found',pos,'%s+%dc'%(pos,len(key)))
            start='%s+%dc'%(pos,len(key))
    search=Tk()
    search.title('Tksearch')
    Label(search,text='请输入要查找的内容：').pack()
    entry3=Entry(search)
    entry3.pack()
    Button(search,text='确定',command=searchbox).pack()
    search.mainloop()

def normal():
    text.tag_remove('found','1.0',END)

def about_this():
    try:
        with open(filename,'r',encoding='UTF-8') as file:
            contennt=file.read()
        text=contennt.rsplit()
        aboutthis=Tk()
        aboutthis.title('关于这个文档')
        Label(aboutthis,text='关于这个文档'+filename+'\n').grid(row=0,column=0)
        Label(aboutthis,text='共有'+str(len(text))+'字').grid(row=1,column=0)
        aboutthis.mainloop()
    except NameError:
        messagebox.showerror(message='您未打开文件或文件错误！')

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
asa1=BooleanVar(root)

entry1=Entry(root)
entry1.pack(fill=X)
entry1.insert("1",'在此输入您要的字体')

entry2=Entry(root)
entry2.pack()
entry2.insert(0,'您的字号')

check=Checkbutton(root,text='加粗',variable=asa1,command=jiacu)
check.pack()

Button(root,text='确定！',command=ok).pack()
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

asa=BooleanVar(root)
asa.set(False)

tanchu=Menu(root,tearoff=0)
tanchu.add_command(label='文字颜色...',command=choosecolor)
tanchu.add_command(label='清除高亮...',command=normal)
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
file2.add_command(label='Tksearch文字查找',command=Tksearch)
file2.add_command(label='关于这个文档...',command=about_this)
root.config(menu=menubar)
menubar.add_cascade(label='帮助(H)',menu=file3)
file3.add_command(label='帮助',command=open_help)
root.config(menu=menubar)
menubar.add_cascade(label='关于(A)',command=about)

text.tag_configure('found',background='yellow')
root.mainloop()
