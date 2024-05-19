
def login():
    Username=Username.get()
    password=password.get()
    if Username=="" and password=="":
        messagebox.showwarning("Error","Please Enter Username and Password")
    elif Username=="":
        messagebox.showwarning("Error","Please Enter Username")    
        clear()
    elif password=="":
        messagebox.showwarning("Error","Please Enter Password")
        clear()
    elif Username!="admin" and password!="123":
        messagebox.showwarning("Error","Invalid Username and Password")
        clear()
    # else: