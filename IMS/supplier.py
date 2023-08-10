from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
from sup_apmc import sup_apmcClass

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #==============================
        # All Variables======

        self.var_searchtxt=StringVar()

        self.var_date=StringVar()
        self.var_supid=StringVar()
        self.var_company=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_cat=StringVar()
        self.cat_list=[]
        self.fetch_cat()
        self.var_desc=StringVar()

        #===searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=470,y=60,width=600,height=90)

        #===options===
        lbl_search=Label(SearchFrame,text="Search By Supplier ID",font=("goudy old style",15),bg="white")
        lbl_search.place(x=10,y=10,width=180)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===title====
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)


        #====content=======

        #===row1====

        lbl_date=Label(self.root,text="Date",font=("goudy old style",15),bg="white").place(x=50,y=60)
    
        txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style",15),bg="lightyellow").place(x=180,y=60,width=180)
    
        #===row2====

        lbl_supid=Label(self.root,text="Supplier ID",font=("goudy old style",15),bg="white").place(x=50,y=100)
        
        txt_supid=Entry(self.root,textvariable=self.var_supid,font=("goudy old style",15),bg="lightyellow").place(x=180,y=100,width=180)
        
        #===row3====

        lbl_company=Label(self.root,text="Company",font=("goudy old style",15),bg="white").place(x=50,y=140)
        
        txt_company=Entry(self.root,textvariable=self.var_company,font=("goudy old style",15),bg="lightyellow").place(x=180,y=140,width=180)
        
        #===row4====

        lbl_name=Label(self.root,text="Supplier Name",font=("goudy old style",15),bg="white").place(x=50,y=180)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=180,width=180)
        
        #===row5====

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=220)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=220,width=180)
        

        #===row6===

        lbl_contact=Label(self.root,text="Category",font=("goudy old style",15),bg="white").place(x=50,y=260)

        cmb_cat=ttk.Combobox(self.root,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=180,y=260,width=200,height=50)
        cmb_cat.current(0)
        
        #===row7====

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=320)
        
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=320,width=350,height=100)
        
        #===buttons====

        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=20,y=450,width=130,height=40)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=160,y=450,width=130,height=40)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=300,y=450,width=130,height=40)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=440,y=450,width=130,height=40)
        # btn_sup_apmc=Button(self.root,text="APMC Supplier",command=self.sup_apmc,font=("goudy old style",15,"bold"),bg="white",cursor="hand2").place(x=10,y=450,width=300,height=30) #image=self.icon_side


        #====Supplier Details===

        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=580,y=180,width=490,height=290)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(sup_frame,columns=("date","supid","company","name","contact","Category","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        self.var_date.set("")
        self.SupplierTable.heading("date",text="Date")
        self.SupplierTable.heading("supid",text="Supplier ID")
        self.SupplierTable.heading("company",text="Company")
        self.SupplierTable.heading("name",text="Name")
        self.SupplierTable.heading("contact",text="Contact")
        self.SupplierTable.heading("Category",text="Category")
        self.SupplierTable.heading("desc",text="Description")
        self.SupplierTable["show"]="headings"

        self.SupplierTable.pack(fill=BOTH,expand=1)

        self.SupplierTable.column("date",width=80)
        self.SupplierTable.column("supid",width=90)
        self.SupplierTable.column("company",width=100)
        self.SupplierTable.column("name",width=200)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("Category",width=100)
        self.SupplierTable.column("desc",width=400)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===============================================================================

    def sup_apmc(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=sup_apmcClass(self.new_win)

    def fetch_cat(self):
        self.cat_list.append("Select")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select m_name from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supid.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_supid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Supplier ID is Alreary Assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier (date,supid,company,name,contact,Category,desc) values(?,?,?,?,?,?,?)",(
                                        self.var_date.get(),
                                        self.var_supid.get(),
                                        self.var_company.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_cat.get(),
                                        self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Succes","Supplier Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_date.set(row[0])
        self.var_supid.set(row[1])
        self.var_company.set(row[2])
        self.var_name.set(row[3])
        self.var_contact.set(row[4])
        self.var_cat.set(row[5])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[6])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supid.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_supid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    cur.execute("Update supplier set  date=?,company=?,name=?,contact=?,Category=?,desc=? where supid=?",(
                                        self.var_date.get(),
                                        self.var_company.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_cat.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_supid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Succes","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_supid.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_desc.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_supid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Supplier ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where supid=?",(self.var_supid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_date.set("")
        self.var_supid.set("")
        self.var_company.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_cat.set("Select")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Supplier ID is Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where supid=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 

if __name__=="__main__":
    root=Tk()
    #root.resizable(False,False)
    obj=supplierClass(root)
    root.mainloop()
