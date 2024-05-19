
from tkinter import*
from tkinter import font
from tkinter.ttk import Combobox
from tkinter import PhotoImage
from PIL import Image,ImageTk



win=Tk()
win.geometry("1000x500+150+75")
win.title("Student information")





# img=Image.open("pic.png")
# img=img.resize((1000,500),Image.ANTIALIAS)
# photo=ImageTk.PhotoImage(img)
# Label(win,image=photo).place(x=0,y=0)

Label(win,text="Student Information",font="arial 25 bold").pack(pady=10)
LabelFrame(win,width=350,height=250,bg="silver",text="Student Detail",font="arial 10 bold").place(x=50,y=60)
LabelFrame(win,width=500,height=80).place(x=230,y=320)
Label(win,text="First Name:",font="arial 15 bold",bg="silver").place(x=80,y=100)
Label(win,text="Last Name:",font="arial 15 bold",bg="silver").place(x=80,y=140)
Label(win,text="E.mail:",font="arial 15 bold",bg="silver").place(x=80,y=180)
Label(win,text="Phone#:",font="arial 15 bold",bg="silver").place(x=80,y=220)
Label(win,text="Gender:",font="arial 15 bold",bg="silver").place(x=80,y=260)
Label(win,text="Entre roll no",font="arial 15 bold").place(x=100,y=420)
Label(win,text="Accept & Continue",font="arial 10 bold").place(x=850,y=470)
Entry(win,width=20,font=20).place(x=200,y=105)
Entry(win,width=20,font=20).place(x=200,y=145)
Entry(win,width=20,font=20).place(x=200,y=185)
Entry(win,width=20,font=20).place(x=200,y=225)
Entry(win,width=20,font=20).place(x=250,y=425)

Radiobutton(win,text="Male",bg="silver").place(x=200,y=260)
Radiobutton(win,text="Female",bg="silver").place(x=300,y=260)

Checkbutton(win).place(x=820,y=470)

Text(win,width=35,height=14,font=20).place(x=600,y=60)


Button(win,text="Save",font="arial 15 bold").place(x=245,y=340)
Button(win,text="Delete",font="arial 15 bold").place(x=350,y=340)
Button(win,text="Update",font="arial 15 bold").place(x=480,y=340)
Button(win,text="Reset",font="arial 15 bold").place(x=630,y=340)
Button(win,text="Search",font="arial 15 bold").place(x=550,y=415)



win.mainloop()