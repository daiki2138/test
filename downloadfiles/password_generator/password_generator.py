ls1='1234567890'
ls2='abcdefghijklmnopqrstuvwzyz'
ls3='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

import tkinter as tk
import random
import pyperclip
from tkinter import messagebox as mb

def ok():
    textbox.delete(0, tk.END)
    sub.destroy()
def no():
    sub.destroy()

def delete():
    global sub
    sub = tk.Toplevel()
    sub.title("DELETE")
    sub.geometry("250x100")
    label = tk.Label(sub, text="削除しますか？")
    label.pack()
    button1 = tk.Button(sub,text="OK",command=ok,bg='#ffffff',height=2,width=5)
    button1.place(x=80, y=20)
    button.pack()
    button2 = tk.Button(sub,text="NO",command=no,bg='#000000',fg='#ffffff',height=2,width=5)
    button2.place(x=130, y=20)
    button.pack()

def back():
    result.destroy()

def back1():
    record.destroy()

def finish():
    result.destroy()
    root.destroy()

def copy():
    pyperclip.copy(pass1)
    result.destroy()
    mb.showinfo("Copy","コピーしました")

def copy1():
    pyperclip.copy(pass1)
    record.destroy()
    mb.showinfo("Copy","コピーしました")

def go():
    ls4=''
    if bln1.get():
        ls4 += ls3
    if bln2.get():
        ls4 += ls2
    if bln3.get():
        ls4 += ls1
    global pass1
    global result
    result = tk.Toplevel()
    if bln1.get() == False and bln2.get() == False and bln3.get() == False:
        result.destroy()
        mb.showerror("Error","チェックボックスにチェックをしてください")
    str = textbox.get()
    if str.isdecimal():
        KEY = int(str)
        if KEY == 0:
            result.destroy()
            mb.showerror("Error","0は入力できません")
        pass1 = ''
        for i in range(0,KEY):
            pass1 = pass1 + random.sample(ls4,1)[0]
    else:
        result.destroy()
        mb.showerror("Error","数字を入力してください")
        textbox.delete(0, tk.END)
    result.title("Result")
    result.geometry("350x100")
    label = tk.Label(result, text="作成したパスワードは    "+pass1+"    です。")
    label.pack()
    button3 = tk.Button(result,text="Copy",command=copy)
    button3.place(x=95, y=30)
    button.pack()
    button4 = tk.Button(result,text="Finish",command=finish)
    button4.place(x=135, y=30)
    button.pack()
    button5 = tk.Button(result,text="Back",command=back)
    button5.place(x=180, y=30)
    button.pack()

def finish():
    end.destroy()
    root.destroy()

def no1():
    end.destroy()

def end():
    global end
    end=tk.Toplevel()
    end.title("Finish")
    end.geometry("250x80")
    label = tk.Label(end, text="終了しますか？")
    label.pack()
    button6 = tk.Button(end,text="はい",command=finish)
    button6.place(x=135, y=30)
    button.pack()
    button7 = tk.Button(end,text="いいえ",command=no1)
    button7.place(x=175, y=30)
    button.pack()

def record():
    global record
    record = tk.Toplevel()
    record.title("Record")
    record.geometry("350x100")
    label = tk.Label(record, text="作成したパスワードは    "+pass1+"    です。")
    label.pack()
    button8 = tk.Button(record,text="Copy",command=copy1)
    button8.place(x=135, y=30)
    button.pack()
    button9 = tk.Button(record,text="Back",command=back1)
    button9.place(x=175, y=30)
    button.pack()

root = tk.Tk()
root.title("Password Generator")
menubar = tk.Menu(root)
root.geometry("350x150")
label = tk.Label(root, text="作成したいパスワードの文字数を入力してください")
label.pack()
textbox = tk.Entry(root)
textbox.pack()

global bln1
global bln2
global bln3
bln1 = tk.BooleanVar()
bln2 = tk.BooleanVar()
bln3 = tk.BooleanVar()


chk = tk.Checkbutton(root,var=bln1, text='大文字を含む')
chk.place(x=60, y=40)
chk = tk.Checkbutton(root,var=bln2, text='小文字を含む')
chk.place(x=60, y=60)
chk = tk.Checkbutton(root,var=bln3, text='数字を含む')
chk.place(x=60, y=80)

button = tk.Button(root,text="OK",command=go,height=2,width=5,bg='#00ffff',fg='#000000')
button.pack()
menubar.add_cascade(label="Delete", command=delete)
menubar.add_cascade(label="END", command=end)
menubar.add_cascade(label="Record", command=record)
root.config(menu=menubar)
root.mainloop()
