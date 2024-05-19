from tkinter import*
from tkinter import messagebox
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from tkinter import font
from msilib.schema import Font
from turtle import width
from tkinter.tix import COLUMN

#==============================New Window============================
def open():
    new_window=Toplevel()
    new_window.geometry("1200x550+100+50")
    new_window.title("New Window")


    #Date Entry
    cal=DateEntry(new_window,font=("none 13"),selectmode="day")
    cal.place(x=980,y=45)

#Label Frame
    LabelFrame(new_window,width=400,height=330).place(x=45,y=110)
        

#Student information Labels
    Label(new_window,text="  STUDENT INFORMATION SYSTEM  ",font="arial 20 bold",fg="black").place(x=400,y=10)
    Label(new_window,text="  Registration New Students  ",font="arial 15 bold",fg="red").place(x=510,y=60)
    Label(new_window,text="Student ID",font="arial 15 bold",fg="black").place(x=50,y=120)
    Label(new_window,text="First Name",font="arial 15 bold",fg="black").place(x=50,y=160)
    Label(new_window,text="Last Name",font="arial 15 bold",fg="black").place(x=50,y=200)
    Label(new_window,text="Birth Date",font="arial 15 bold",fg="black").place(x=50,y=240)
    Label(new_window,text="Gender",font="arial 15 bold",fg="black").place(x=50,y=280)
    Label(new_window,text="Address",font="arial 15 bold",fg="black").place(x=50,y=320)
    Label(new_window,text="Phone#",font="arial 15 bold",fg="black").place(x=50,y=360)
    Label(new_window,text="Admission Date",font="arial 15 bold",fg="black").place(x=50,y=400)
    Label(new_window,text="Discription",font="arial 10 ",fg="black").place(x=800,y=260)
    

    #Entry Box
    std=Entry(new_window,font=15,width=25,bg="silver").place(x=200,y=125)
    ft=Entry(new_window,font=15,width=25,bg="silver").place(x=200,y=165)
    lt=Entry(new_window,font=15,width=25,bg="silver").place(x=200,y=205)
    bd=Entry(new_window,font=15,width=25,bg="silver").place(x=200,y=245)
    ad=Entry(new_window,font=15,width=25,bg="silver").place(x=200,y=325)
    ph=Entry(new_window,font=15,width=25,bg="silver").place(x=200,y=365)
    am=Entry(new_window,font=15,width=20,bg="silver").place(x=220,y=405)

    #combo box in gender
    comb=Combobox(new_window,font=15,width=22,values=["select option","Male","Female"],state="readonly")
    comb.place(x=200,y=285)
    comb.current(0)

    #text box

    Text(new_window,width=40,height=10).place(x=800,y=280)


    #buttons

    Button(new_window,text="Save",font="arial 15 bold",bg="silver",fg="red").place(x=200,y=450)
    Button(new_window,text="Delete",font="arial 15 bold",bg="silver",fg="red").place(x=300,y=450)
    Button(new_window,text="Update",font="arial 15 bold",bg="silver",fg="red").place(x=420,y=450)
    Button(new_window,text="Reset",font="arial 15 bold",bg="silver",fg="red",command=data_reset).place(x=550,y=450)
    Button(new_window,text="Exit",font="arial 15 bold",bg="silver",fg="red").place(x=1100,y=480)


    #Check_button
    Checkbutton(new_window,text="applay Now").place(x=100,y=500)
#=================================Main Window==========================================
win=Tk()
Button(text="open",command=open).pack()
win.geometry("500x400")
win.title("Login Page")
win.geometry("1200x600+100+50")
#----------------------------
Frame_login=Frame(win,bg="white")
Frame_login.place(x=300,y=100,height=400,width=650)
#----------------------------
title=Label(Frame_login,text="Login Here",font=("impact 35 bold"),fg="#d77337",bg="white")
title.place(x=200,y=30)
#----------------------------
usr=Label(Frame_login,text="User Name",font=("arial 15"),fg="black",bg="white")
usr.place(x=100,y=150)
#---------------------------
pas=Label(Frame_login,text="Password",font=("arial 15"),fg="black",bg="white")
pas.place(x=100,y=250)
#---------------------------
usrr=Entry(Frame_login,width=40,bg="silver",font="bold 13")
usrr.place(x=100,y=200)
#---------------------------
pasr=Entry(Frame_login,width=40,bg="silver",font="bold 13")
pasr.place(x=100,y=300)

def logi():

    user_name=usrr.get()
    password=pasr.get()
    if user_name=="admin" and password=="123":
        messagebox.showinfo("wellcome","successful login")
    elif user_name=="" and password=="":
        messagebox.showerror("Error","Required fields")
    elif user_name=="":
        messagebox.showerror("Error","Please Enter User name")
    elif password=="":
        messagebox.showerror("Error","Please Enter password")
    elif user_name!="admin" and password!="123":
        messagebox.showerror("Error","invalid user name and password")
    elif user_name!="admin":
        messagebox.showerror("Error","invalid user name")
    elif password!="123":
        messagebox.showerror("Error","invalid password")
Button(Frame_login,text="Login",font="arial 20 bold",fg="#d77337",command=logi).place(x=100,y=350)
#--------------------Reset button---------------------------------------------------------
def reset():
    usrr.delete(0,END)
    pasr.delete(0,END)
    
Button(Frame_login,text="Reset",font="arial 20 bold",fg="#d77337",command=reset).place(x=250,y=350)
#--------------------cancel button---------------------------------------------------------
def cancl():
    status=messagebox.askyesno("question","Do you want to close the window")
    if status==True:
        win.destroy()
    else:
        messagebox.showwarning("Warning","please login again")
Button(Frame_login,text="cancel",font="arial 20 bold",fg="#d77337",command=cancl).place(x=380,y=350)

win.mainloop()