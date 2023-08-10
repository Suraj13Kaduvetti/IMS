from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class sup_apmcClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | By Ayush")
        self.root.config(bg="white")
        self.root.focus_force()
        #==============================
        # All Variables======

        self.var_searchtxt=StringVar()

        self.var_date=StringVar()
        self.var_sup_invoice=StringVar()
        self.var_company=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_gala_no=StringVar() 
        self.var_desc=StringVar()

        #===searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=470,y=60,width=600,height=90)

        #===options===
        lbl_search=Label(SearchFrame,text="Search By Invoice No.",font=("goudy old style",15),bg="white")
        lbl_search.place(x=10,y=10,width=180)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #===title====
        title=Label(self.root,text="APMC Supplier Details",font=("goudy old style",20,"bold"),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)


        #====content=======

        #===row1====

        lbl_date=Label(self.root,text="Date",font=("goudy old style",15),bg="white").place(x=50,y=60)
    
        txt_date=Entry(self.root,textvariable=self.var_date,font=("goudy old style",15),bg="lightyellow").place(x=180,y=60,width=180)
    
        #===row2====

        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=100)
        
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=180,y=100,width=180)
        
        #===row3====

        lbl_company=Label(self.root,text="Company",font=("goudy old style",15),bg="white").place(x=50,y=140)
        
        txt_company=Entry(self.root,textvariable=self.var_company,font=("goudy old style",15),bg="lightyellow").place(x=180,y=140,width=180)
        
        #===row4====

        lbl_name=Label(self.root,text="Supplier Name",font=("goudy old style",15),bg="white").place(x=50,y=180)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=180,y=180,width=180)
        
        #===row5====

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=220)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=180,y=220,width=180)
        
        #===row5====

        lbl_gala_no=Label(self.root,text="Gala No.",font=("goudy old style",15),bg="white").place(x=50,y=260)
        
        txt_gala_no=Entry(self.root,textvariable=self.var_gala_no,font=("goudy old style",15),bg="lightyellow").place(x=180,y=260,width=180)

        #===row6====

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=300)
        
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=300,width=350,height=100)
        
        #===buttons====

        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=80,y=440,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=200,y=440,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=320,y=440,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=440,y=440,width=110,height=28)
        btn_prod_apmc=Button(self.root,text="APMC Product",font=("goudy old style",15,"bold"),bg="white",cursor="hand2").place(x=50,y=480,width=300,height=20) 


        #====Supplier Details===

        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=580,y=180,width=490,height=290)

        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.Sup_ApmcTable=ttk.Treeview(sup_frame,columns=("date","invoice","company","name","contact","gala","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Sup_ApmcTable.xview)
        scrolly.config(command=self.Sup_ApmcTable.yview)
        self.var_date.set("")
        self.Sup_ApmcTable.heading("date",text="Date")
        self.Sup_ApmcTable.heading("invoice",text="Invoice No.")
        self.Sup_ApmcTable.heading("company",text="Company")
        self.Sup_ApmcTable.heading("name",text="Name")
        self.Sup_ApmcTable.heading("contact",text="Contact")
        self.Sup_ApmcTable.heading("gala",text="Gala No.")
        self.Sup_ApmcTable.heading("desc",text="Description")
        self.Sup_ApmcTable["show"]="headings"

        self.Sup_ApmcTable.pack(fill=BOTH,expand=1)

        self.Sup_ApmcTable.column("date",width=80)
        self.Sup_ApmcTable.column("invoice",width=90)
        self.Sup_ApmcTable.column("company",width=100)
        self.Sup_ApmcTable.column("name",width=200)
        self.Sup_ApmcTable.column("contact",width=100)
        self.Sup_ApmcTable.column("gala",width=90)
        self.Sup_ApmcTable.column("desc",width=400)
        self.Sup_ApmcTable.pack(fill=BOTH,expand=1)
        self.Sup_ApmcTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#===============================================================================
    
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from sup_apmc where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice no. is Alreary Assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into sup_apmc (date,invoice,company,name,contact,gala,desc) values(?,?,?,?,?,?,?)",(
                                        self.var_date.get(),
                                        self.var_sup_invoice.get(),
                                        self.var_company.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_gala_no.get(),
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
            cur.execute("Select * from sup_apmc")
            rows=cur.fetchall()
            self.Sup_ApmcTable.delete(*self.Sup_ApmcTable.get_children())
            for row in rows:
                self.Sup_ApmcTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.Sup_ApmcTable.focus()
        content=(self.Sup_ApmcTable.item(f))
        row=content['values']
        #print(row)
        self.var_date.set(row[0])
        self.var_sup_invoice.set(row[1])
        self.var_company.set(row[2])
        self.var_name.set(row[3])
        self.var_contact.set(row[4])
        self.var_gala_no.set(row[5])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[6])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from sup_apmc where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no",parent=self.root)
                else:
                    cur.execute("Update sup_apmc set  date=?,company=?,name=?,contact=?,gala=?,desc=? where invoice=?",(
                                        self.var_date.get(),
                                        self.var_company.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.var_gala_no.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_sup_invoice.get()
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
            if self.var_sup_invoice.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from sup_apmc where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice no.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from sup_apmc where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_date.set("")
        self.var_sup_invoice.set("")
        self.var_company.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_gala_no.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. is Required",parent=self.root)
            else:
                cur.execute("Select * from sup_apmc where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.Sup_ApmcTable.delete(*self.Sup_ApmcTable.get_children())
                    self.Sup_ApmcTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 

if __name__=="__main__":
    root=Tk()
    #root.attributes('-fullscreen',True)
    #root.resizable(False,False)
    obj=sup_apmcClass(root)
    root.mainloop()