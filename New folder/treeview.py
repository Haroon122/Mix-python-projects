from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
import mysql.connector
class tree:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Test")
        self.root.config(bg="white")
        self.root.resizable(False,False)

#######################veriables########################################################

        self.var_name=StringVar()
        self.var_fname=StringVar()
        self.var_ph=StringVar()
        self.var_ad=StringVar()
        self.var_search_comb=StringVar()
        self.var_search_entry=StringVar()


###########################################################################################33
        frm=LabelFrame(self.root,bg="white",bd=3)
        frm.place(x=100,y=200,width=1200,height=400)

        scroll_x=ttk.Scrollbar(frm,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(frm,orient=VERTICAL)

        self.tr=ttk.Treeview(frm,column=("name","fname","ph","ad"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.tr.xview)
        scroll_y.config(command=self.tr.yview)

        self.tr.heading("name",text="Name")
        self.tr.heading("fname",text="Father Name")
        self.tr.heading("ph",text="Phone")
        self.tr.heading("ad",text="Address")
        self.tr["show"]="headings"

        self.tr.column("name",width=100)
        self.tr.column("fname",width=100)
        self.tr.column("ph",width=100)
        self.tr.column("ad",width=100)

        self.tr.pack(expand=1,fill=BOTH)
        self.fetchData()
        self.tr.bind("<ButtonRelease>",self.getData)
########################################################################################

        en1=Entry(self.root,textvariable=self.var_name,bd=2,relief=RIDGE,bg="white")
        en1.place(x=200,y=100)
        en2=Entry(self.root,textvariable=self.var_fname,bd=2,relief=RIDGE,bg="white")
        en2.place(x=200,y=150)
        en3=Entry(self.root,textvariable=self.var_ph,bd=2,relief=RIDGE,bg="white")
        en3.place(x=500,y=100)
        en4=Entry(self.root,textvariable=self.var_ad,bd=2,relief=RIDGE,bg="white")
        en4.place(x=500,y=150)     
########################################################################################

        l1=Label(text="Name",bg="white",fg="darkgreen")
        l1.place(x=200,y=80)  
        l2=Label(text="Father Name",bg="white",fg="darkgreen")
        l2.place(x=200,y=125)   
        l3=Label(text="Phone",bg="white",fg="darkgreen")
        l3.place(x=500,y=80)   
        l4=Label(text="Address",bg="white",fg="darkgreen")
        l4.place(x=500,y=125)   
#######################################################################################

        b1=Button(self.root,command=self.add,text="Save",bg="white",fg="red")
        b1.place(x=700,y=100,width=100)
        b2=Button(self.root,command=self.updatedata,text="Update",bg="white",fg="red")
        b2.place(x=700,y=120,width=100)
        b3=Button(self.root,command=self.dlt,text="Delete",bg="white",fg="red")
        b3.place(x=700,y=140,width=100)
        b4=Button(self.root,command=self.clr,text="Clear",bg="white",fg="red")
        b4.place(x=700,y=160,width=100)
        s_btn=Button(self.root,command=self.srch,text="Search",bg="white",fg="red")
        s_btn.place(x=1200,y=50,width=100)
        show_btn=Button(self.root,command=self.fetchData,text="Show",bg="white",fg="red")
        show_btn.place(x=1250,y=50,width=100)                  
######################################################################################
        comb=ttk.Combobox(self.root,textvariable=self.var_search_comb,state="readonly")
        comb["values"]=("Select Option","Name","Phone")
        comb.current(0)
        comb.place(x=900,y=50,width=100)

        s_entry=Entry(self.root,textvariable=self.var_search_entry,bd=2,relief=RIDGE,bg="white")
        s_entry.place(x=1000,y=50) 
#add query
    def add(self):
        if self.var_name.get()=="" or self.var_fname.get()=="" or self.var_ph.get()=="" or self.var_ad.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="test")
                cur=con.cursor()

                query= (
                    "INSERT INTO testing SET "
                    "name=%s, "
                    "fname=%s, "
                    "phone=%s, "
                    "address=%s "

                )

                data= (

                    self.var_name.get(),
                    self.var_fname.get(),
                    self.var_ph.get(),
                    self.var_ad.get()
                )

                cur.execute(query,data)
                con.commit()
                messagebox.showinfo("info","Data Added")
                self.fetchData()
                con.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error:{str(e)}")

#fetch data

    def fetchData(self):
        try:
            con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="test")
            cur=con.cursor()
            cur.execute("select * from testing")
            data=cur.fetchall()
            self.tr.delete(*self.tr.get_children())
            if len (data)!=0:
                for i in data:
                    self.tr.insert("",END,values=i)
                con.commit()
            con.close()
        except Exception as e:
            messagebox.showerror("Error",f"Error:{str(e)}")    

#get data


    def getData(self,event=""):
        cur_f=self.tr.focus()
        content=self.tr.item(cur_f)
        data=content["values"]
        self.var_name.set(data[0])
        self.var_fname.set(data[1])
        self.var_ph.set(data[2])
        self.var_ad.set(data[3])
#update data
    def updatedata(self):
        if self.var_name.get()=="" or self.var_fname.get()=="" or self.var_ph.get()=="" or self.var_ad.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                updt=messagebox.askyesno("ask","do you want to update")
                if updt>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="test")
                    cur=con.cursor()
                    query= (
                        "UPDATE testing SET "
                        "name=%s, "
                        "fname=%s, "
                        "address=%s "
                        "WHERE phone=%s "
                     )
                    data= (

                        self.var_name.get(),
                        self.var_fname.get(),
                        self.var_ad.get(),
                        self.var_ph.get()
                    )
                    cur.execute(query,data)
                    con.commit()
                    self.fetchData()
                    con.close()
                else:
                    return
            except Exception as e:
                messagebox.showerror("ERROR",f"Error:{str(e)}")

#delete data
    def dlt(self):
        if self.var_name.get()=="" or self.var_fname.get()=="" or self.var_ph.get()=="" or self.var_ad.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                dltee=messagebox.askyesno("ask","do you want to Delete")
                if dltee>0:
                    con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="test")
                    cur=con.cursor()
                    sql="delete from testing where phone=%s"
                    val=(self.var_ph.get(),)
                    cur.execute(sql,val)
                    con.commit()
                    self.fetchData()
                    con.close()
                    messagebox.showinfo("info","Data Deleted")
                else:
                    if  not dltee:
                        return
            except Exception as e:
                messagebox.showerror("ERROR",f"Error:{str(e)}")

#clear
    def clr(self):
        self.var_name.set("")
        self.var_fname.set("")
        self.var_ph.set("")
        self.var_ad.set("")

#search
    def srch(self):
        if self.var_search_comb.get()=="Select Option" or self.var_search_entry.get()=="":
            messagebox.showerror("Error","Please fill Search entry fields")
        else:
            try:
                con=mysql.connector.connect(host="localhost",username="root",password="h@Roon#123Abc",database="test")
                cur=con.cursor()
                if self.var_search_comb.get()=="Name":
                    query="SELECT * FROM testing WHERE name LIKE %s"
                elif self.var_search_comb.get()=="Phone":
                    query="SELECT * FROM testing WHERE phone LIKE %s"
                search_value = f"%{self.var_search_entry.get()}%"
                cur.execute(query,(search_value,))
                data=cur.fetchall()

                self.tr.delete(*self.tr.get_children())
                if len (data) !=0:
                    for i in data:
                        self.tr.insert("",END,values=i)
                con.close()
            except Exception as e:
                messagebox.showerror("Error",f"Error:{str(e)}")










if __name__=="__main__":
    root=Tk()
    obj=tree(root)
    root.mainloop() 