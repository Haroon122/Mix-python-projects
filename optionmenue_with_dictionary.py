
from tkinter import*
win=Tk()

win.geometry("500x300+100+100")


Options=StringVar(win)
mydict={1:"englisf",2:"urdu",3:"math"}
Options.set("languge")


#we use with key & values


Opt=OptionMenu(win,Options,*mydict.keys())



Opt.place(x=30,y=30)
win.mainloop()