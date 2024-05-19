from tkinter import*
win=Tk()
win.geometry("900x500+200+50")
Label(win,text="user",fg="red",font="bold 20").place(x=100,y=80)
Label(win,text="password",fg="red",font="bold 20").place(x=100,y=120)
Entry(win,width=20,font="bold 20").place(x=250,y=80)
Entry(win,width=20,font="bold 20").place(x=250,y=120)
global user , passwrd
def login():
    user = StringVar()
    passwrd = StringVar()
    if user.get()=="admin" and passwrd.get() == "12345":
      
        if user.get()!="admin" and passwrd.get() != "12345":
            messagebox.showerror("ERROR","Invalid1 username and password")
        elif user.get()=="" or passwrd.get() == "":
         messagebox.showerror("ERROR","Invalid2 username and password")
    elif user.get()=="":
         messagebox.showerror("ERROR","Invalid3 username and password")
    elif passwrd.get()=="":
        messagebox.showerror("ERROR","Invalid4 username and password")
    else:
          messagebox.showinfo("Sucess","loged")
Button(win,text="ok",font="bold 20",fg="red",command=login).place(x=250,y=180)



        



win.mainloop()