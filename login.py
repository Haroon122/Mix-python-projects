
# from ast import And
# from ssl import _PasswordType
from tkinter import *
# from tkinter import font
from tkinter.ttk import Combobox
from tkinter import messagebox
win=Tk()
win.geometry("1000x500+150+75")
win.title("Student information")
win.config(bg="#000000")
global user , passwrd
def login():
    user = StringVar()
    passwrd = StringVar()
 
    if user.get()=="admin" and passwrd.get() == "12345":
        messagebox.showinfo("Sucess","loged")
        if user.get()!="admin" and passwrd.get() != "12345":
            messagebox.showerror("ERROR","Invalid1 username and password")
    elif user.get()=="" or passwrd.get() == "":
         messagebox.showerror("ERROR","Invalid2 username and password")
    elif user.get()=="":
         messagebox.showerror("ERROR","Invalid3 username and password")
    elif passwrd.get()=="":
        messagebox.showerror("ERROR","Invalid4 username and password")
    # else:
    #     messagebox.showinfo("Sucess","loged")
    
Label(win,text="username",font="arial 25 bold").pack(pady=10)
Label(win,text="password",font="arial 25 bold").pack(pady=100)
Entry(win,width=20,font=20).place(x=400,y=105)
Entry(win,width=20,font=20).place(x=400,y=245)
Button(win,text="Save",font="arial 15 bold",command=login).place(x=500,y=340)


# LabelFrame(win,width=350,height=250,bg="silver",text="Student Detail",font="arial 10 bold").place(x=50,y=60)
win.mainloop()