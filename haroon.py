from tkinter import*
from tkinter import font
from tkinter.ttk import Combobox
win=Tk()
win.geometry("1000x500+150+75")
win.title("Student information")
Label(win,text="Student Information",font="arial 25 bold").pack(pady=10)
LabelFrame(win,width=350,height=250,bg="silver",text="Student Detail",font="arial 10 bold").place(x=50,y=60)
Label(win,text="First Name:",font="arial 15 bold",bg="silver").place(x=80,y=100)
Label(win,text="Last Name:",font="arial 15 bold",bg="silver").place(x=80,y=140)
Label(win,text="E.mail:",font="arial 15 bold",bg="silver").place(x=80,y=180)
Label(win,text="Phone#:",font="arial 15 bold",bg="silver").place(x=80,y=220)
Label(win,text="Gender:",font="arial 15 bold",bg="silver").place(x=80,y=260)
Entry(win,width=20,font=20).place(x=200,y=105)
Entry(win,width=20,font=20).place(x=200,y=145)
Entry(win,width=20,font=20).place(x=200,y=185)
Entry(win,width=20,font=20).place(x=200,y=225)
comb_box=Combobox(win,width=18,font=20,values=["Select option","Male","Female"],state="readonly")
comb_box.place(x=200,y=265)
comb_box.current(0)
LabelFrame(win,width=500,height=80).place(x=230,y=320)
Button(win,text="Save",font="arial 15 bold").place(x=245,y=340)
Button(win,text="Delete",font="arial 15 bold").place(x=350,y=340)
Button(win,text="Update",font="arial 15 bold").place(x=480,y=340)
Button(win,text="Reset",font="arial 15 bold").place(x=630,y=340)
Label(win,text="Entre roll no",font="arial 15 bold").place(x=100,y=420)
Entry(win,width=20,font=20).place(x=250,y=425)
Button(win,text="Search",font="arial 15 bold").place(x=550,y=415)



win.mainloop()