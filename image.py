
from tkinter import*
from tkinter import PhotoImage
from PIL import Image,ImageTk


win=Tk()
win.geometry("1000x500+100+75")
win.config(bg="white")

"""img=Image.open("pic.png")
img=img.resize((1000,500),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)
Label(win,image=photo).place(x=0,y=0)"""
Image=PhotoImage(file="D:\python projects\python\pp.png")

win.mainloop()