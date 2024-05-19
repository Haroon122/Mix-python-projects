

from tkinter import*
from tkinter.ttk import Combobox

Win =Tk()
Win.geometry("1200x600+100+50")
Win.title("My First Project")
Win.resizable(False,False)
Win.config(bg="black")

Label(Win,text="Forget password",bg="black",fg="yellow",font="none 20 bold").pack(pady=50)
Label(Win,text="security question",bg="black",fg="yellow",font="none 15 bold").place(x=500,y=200)
Label(Win,text="security anwser",bg="black",fg="yellow",font="none 15 bold").place(x=500,y=300)
Label(Win,text="new password",bg="black",fg="yellow",font="none 15 bold").place(x=500,y=400)

Combobox(Win,width=30,font=15).place(x=700,y=200)


Combobox(Win,width=30,font=15).place(x=700,y=300)

Entry(Win,font=20,width=31).place(x=700,y=400)
Button(text="Reset",font="none 20 bold",fg="white",bg="red").place(x=600,y=500)

Win.mainloop()
