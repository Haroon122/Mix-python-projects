from cgitb import text
from tkinter import*
from tkinter.ttk import Combobox
Win=Tk()
Win.geometry("1000x500+200+50")
Win.config(bg="black")
Win.title("Managment System")

Label(Win,text="Managment System",font="arial 30 bold",fg="white",bg="black").pack(pady=20)
Label(Win,text="First Name :",font="arial 15 bold",bg="black",fg="white").place(x=100,y=100)
Label(Win,text="Last Name :",font="arial 15 bold",bg="black",fg="white").place(x=100,y=150)
Label(Win,text="E.mail :",font="arial 15 bold",bg="black",fg="white").place(x=100,y=200)
Label(Win,text="Phone No # :",font="arial 15 bold",bg="black",fg="white").place(x=100,y=250)
Label(Win,text="Gender :",font="arial 15 bold",bg="black",fg="white").place(x=100,y=300)

Entry(Win,font=25,width=25).place(x=300,y=105)
Entry(Win,font=25,width=25).place(x=300,y=150)
Entry(Win,font=25,width=25).place(x=300,y=200)
Entry(Win,font=25,width=25).place(x=300,y=250)

Combobox(Win,font=25,width=23).place(x=300,y=300)

Button(Win,text="Add",font="arial 25 bold",bg="white",fg="black").place(x=303,y=350)
Button(Win,text="Update",font="arial 25 bold",bg="white",fg="black").place(x=403,y=350)
Button(Win,text="Delete",font="arial 25 bold",bg="white",fg="black").place(x=550,y=350)
Button(Win,text="Exit",font="arial 25 bold",bg="white",fg="black").place(x=850,y=430)


Win.mainloop()