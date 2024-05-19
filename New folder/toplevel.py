from distutils.cmd import Command
from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import messagebox
win = Tk()




    
win.geometry("900x450+280+50")
win.config(bg="sky blue")
win.title("login page")

Username=StringVar()
Passwrd=StringVar()
Label(win,text="  STUDENT INFORMATION SYSTEM  ",font="arial 20 bold",fg="black").place(x=200,y=10)
Label(win,text="Username",font="arial 15 bold").place(x=250,y=100)
Label(win,text="Password",font="arial 15 bold").place(x=250,y=200)
Entry(win,font=30,width=25,textvariable=Username).place(x=400,y=105)
Entry(win,font=30,width=25,textvariable=Passwrd).place(x=400,y=205)

def login():
    u=Username.get()
    p=Passwrd.get()
    if u=="abc" and p=="123":
        messagebox.showinfo("Login Status","you have loged in.")
    else:
        messagebox.showerror(title="login Error",message="usernname/password is incorect")

Button(win,text="Login",font="bold 14",command=toplevel_win).place(x=300,y=350)
def toplevel_win():
    win2=Toplevel()
    win2.geometry("1200x550+100+50")
    win2.config(bg="#C7F2A4")
    #Date Entry
    cal=DateEntry(win2,font=("none 13"),selectmode="day")
    cal.place(x=980,y=45)

    #student image
    img2=Image.open('sss.jpg')
    img2=img2.resize((250,150),Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(img2)
    Label(win2,image=photo2).place(x=865,y=95)

    #Label Frame
    LabelFrame(win2,width=400,height=330).place(x=45,y=110)

     #combo box in gender
    comb=Combobox(win2,font=15,width=22,values=["select option","Male","Female"],state="readonly")
    comb.place(x=200,y=285)
    comb.current(0)

    #text box

    Text(win2,width=40,height=10).place(x=800,y=280)

        #  Check_button
    Checkbutton(win2,text="applay Now").place(x=100,y=500)



    #Student information Labels
    Label(win2,text="  STUDENT INFORMATION SYSTEM  ",font="arial 20 bold",fg="black").place(x=400,y=10)
    Label(win2,text="  Registration New Students  ",font="arial 15 bold",fg="red").place(x=510,y=60)
    Label(win2,text="Student ID",font="arial 15 bold",fg="black",bg="white").place(x=50,y=120)
    Label(win2,text="First Name",font="arial 15 bold",fg="black",bg="white").place(x=50,y=160)
    Label(win2,text="Last Name",font="arial 15 bold",fg="black",bg="white").place(x=50,y=200)
    Label(win2,text="Birth Date",font="arial 15 bold",fg="black",bg="white").place(x=50,y=240)
    Label(win2,text="Gender",font="arial 15 bold",fg="black",bg="white").place(x=50,y=280)
    Label(win2,text="Address",font="arial 15 bold",fg="black",bg="white").place(x=50,y=320)
    Label(win2,text="Phone#",font="arial 15 bold",fg="black",bg="white").place(x=50,y=360)
    Label(win2,text="Admission Date",font="arial 15 bold",fg="black",bg="white").place(x=50,y=400)
    Label(win2,text="Discription",font="arial 10 ",fg="black",bg="white").place(x=800,y=260)



    rst=StringVar()
    ft_name=StringVar()
    lt_name=StringVar()
    adrs=StringVar()
    ph_no=StringVar()
    ad_dt=StringVar()


    #Entry Box
    Entry(win2,font=15,width=25,bg="silver").place(x=200,y=125)
    Entry(win2,textvariable=lt_name,font=15,width=25,bg="silver").place(x=200,y=165)
    Entry(win2,textvariable=adrs,font=15,width=25,bg="silver").place(x=200,y=205)
    Entry(win2,textvariable=ph_no,font=15,width=25,bg="silver").place(x=200,y=245)
    Entry(win2,textvariable=ad_dt,font=15,width=25,bg="silver").place(x=200,y=325)
    Entry(win2,textvariable=ft_name,font=15,width=25,bg="silver").place(x=200,y=365)
    Entry(win2,textvariable=rst,font=15,width=20,bg="silver").place(x=220,y=405)

    Button(win2,text="Save",font="arial 15 bold",bg="silver",fg="red").place(x=200,y=450)
    Button(win2,text="Delete",font="arial 15 bold",bg="silver",fg="red").place(x=300,y=450)
    Button(win2,text="Update",font="arial 15 bold",bg="silver",fg="red").place(x=420,y=450)
    Button(win2,text="Exit",font="arial 15 bold",bg="silver",fg="red").place(x=1100,y=480)
    






def reset():
    # rst.set("")
        ft_name.set("")
        lt_name.set("")
        adrs.set("")
        ph_no.set("")
        ad_dt.set("")
        rst.set("")
Button(win2,command=reset,text="Reset",font="arial 15 bold",bg="silver",fg="red").place(x=550,y=450)

win.mainloop()