from tkinter import Tk, Label, PhotoImage

win = Tk()
win.title("Label with Image")
win.geometry("50x900+70+50")

# Load an image
image = PhotoImage(file="D:\python projects\python\pp.png")  # Replace "your_image.png" with the actual image file path

# Label with text and image
label_text = "Hello Tkinter!"
label = Label(win, text=label_text, font=("Helvetica", 20), fg="white", bg=None, bd=5, relief="solid", padx=10, pady=5, compound="left", image=image)
label.pack()

win.mainloop()
