from tkinter import*
from tkinter import messagebox

win=Tk()
win.title("login Screen")
win.geometry("600x300")
l1=Label(win,text="Username:",font="arial 14 bold")
l2=Label(win,text="Password:",font="arial 14 bold")
l1.grid(row=0,column=0,padx=5,pady=5)
l2.grid(row=1,column=0,padx=5,pady=5)

Username=StringVar()
Password=StringVar()
t1=Entry(win,textvariable=Username,font="14",bg="silver")
t2=Entry(win,textvariable=Password,font="14",bg="silver",show='*')  #password box will with*
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)


def login():
    if Username.get()=="Admin" and Password.get()=="1234":
        messagebox.showinfo(title="Login Status",message="you have loged in.")
    else:
        messagebox.showerror(title="login Error",message="usernname/password is incorect")


b1=Button(win,command=login,text="Login",font="arial 10 bold")


def cancel():
    status=messagebox.askyesno(title="Question",message="Do you want to close the window")
    if status==True:
        win.destroy()
    else:
        messagebox.showwarning(title="warrning Message",message="please login again!!")
        


b2=Button(win,command=cancel,text="Cancel",font="arial 10 bold",cursor="hand2")
b1.grid(row=2,column=1,sticky=W)
b2.grid(row=2,column=1,sticky=E)






win.mainloop()
