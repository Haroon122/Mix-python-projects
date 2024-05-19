
from tkinter import*
win=Tk()

win.geometry("500x300+100+100")
Options=StringVar(win)
mylist=["englisf","urdu","math"]
Options.set("haroon")
OptMenu=OptionMenu(win,Options,*mylist)
OptMenu.grid(row=0,column=0,padx=30,pady=30)
win.mainloop()