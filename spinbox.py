from tkinter import*
from tkcalendar import DateEntry
win=Tk()
win.geometry("300x200")
cal=Spinbox(win,values=["a","b","c","d"],font="poppins 20 bold")
cal.grid(row=0,column=0,padx=30,pady=30)
win.mainloop()