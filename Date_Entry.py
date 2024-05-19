
from tkinter import*
from tkcalendar import DateEntry
win=Tk()
win.geometry("300x200")
cal=DateEntry(win,selectmode="day")
cal.grid(row=0,column=0,padx=30,pady=30)
win.mainloop()