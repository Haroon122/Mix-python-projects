
from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter.tix import COLUMN
from tkinter.ttk import Combobox
from turtle import width
from tkcalendar import DateEntry
from tkinter import PhotoImage
from PIL import Image,ImageTk
win=Tk()
win.geometry("1200x550+100+50")
win.config(bg="white")
win.title("Student Information")



#Date Entry
cal=DateEntry(win,font=("none 13"),selectmode="day")
cal.place(x=980,y=45)

#Label Frame
LabelFrame(win,width=400,height=330).place(x=45,y=110)


#Student information Labels
Label(win,text="  STUDENT INFORMATION SYSTEM  ",font="arial 20 bold",fg="black").place(x=400,y=10)
Label(win,text="  Registration New Students  ",font="arial 15 bold",fg="red").place(x=510,y=60)
Label(win,text="Student ID",font="arial 15 bold",fg="black",bg="white").place(x=50,y=120)
Label(win,text="First Name",font="arial 15 bold",fg="black",bg="white").place(x=50,y=160)
Label(win,text="Last Name",font="arial 15 bold",fg="black",bg="white").place(x=50,y=200)
Label(win,text="Birth Date",font="arial 15 bold",fg="black",bg="white").place(x=50,y=240)
Label(win,text="Gender",font="arial 15 bold",fg="black",bg="white").place(x=50,y=280)
Label(win,text="Address",font="arial 15 bold",fg="black",bg="white").place(x=50,y=320)
Label(win,text="Phone#",font="arial 15 bold",fg="black",bg="white").place(x=50,y=360)
Label(win,text="Admission Date",font="arial 15 bold",fg="black",bg="white").place(x=50,y=400)
Label(win,text="Discription",font="arial 10 ",fg="black",bg="white").place(x=800,y=260)


#Entry Box
Entry(win,font=15,width=25,bg="silver").place(x=200,y=125)
Entry(win,font=15,width=25,bg="silver").place(x=200,y=165)
Entry(win,font=15,width=25,bg="silver").place(x=200,y=205)
Entry(win,font=15,width=25,bg="silver").place(x=200,y=245)
Entry(win,font=15,width=25,bg="silver").place(x=200,y=325)
Entry(win,font=15,width=25,bg="silver").place(x=200,y=365)
Entry(win,font=15,width=20,bg="silver").place(x=220,y=405)

#combo box in gender
comb=Combobox(win,font=15,width=22,values=["select option","Male","Female"],state="readonly")
comb.place(x=200,y=285)
comb.current(0)

#text box

Text(win,width=40,height=10).place(x=800,y=280)


#buttons

Button(win,text="Save",font="arial 15 bold",bg="silver",fg="red").place(x=200,y=450)
Button(win,text="Delete",font="arial 15 bold",bg="silver",fg="red").place(x=300,y=450)
Button(win,text="Update",font="arial 15 bold",bg="silver",fg="red").place(x=420,y=450)
Button(win,text="Reset",font="arial 15 bold",bg="silver",fg="red").place(x=550,y=450)
Button(win,text="Exit",font="arial 15 bold",bg="silver",fg="red").place(x=1100,y=480)


#Check_button
Checkbutton(win,text="applay Now").place(x=100,y=500)



win.mainloop()