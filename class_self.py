from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
class windw():
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x680+0+0")
        self.root.title("Employe Management System")


        lbl_title=Label(self.root,text="EMPLOYE MANAGMENT SYSTEM",font="arial 37 bold",fg="dark blue",bg="white")
        lbl_title.place(x=0,y=0,width=1350,height=50)


        img_logo=Image.open("logo image.webp")
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.Photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.Photo_logo)
        self.logo.place(x=200,y=0,width=50,height=50)









if __name__ == '__main__':
    root =Tk()
    obj = windw(root)
    root.mainloop()