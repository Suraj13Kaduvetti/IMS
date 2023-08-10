from math import prod
from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
#from ttkwidgets.autocomplete import AutocompleteEntry
from prod_apmc import prod_apmcClass

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #==============================

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_date=StringVar()
        self.var_hsn=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_mrp=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=450,height=480)

        #===title====
        title=Label(product_frame,text="Manage Products Details",font=("goudy old style",18),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)

        #===column1=====

        lbl_date=Label(product_frame,text="Date",font=("goudy old style",18),bg="white").place(x=30,y=40)
        lbl_pid=Label(product_frame,text="HSN Code",font=("goudy old style",18),bg="white").place(x=30,y=80)
        lbl_category=Label(product_frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=120) 
        lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=30,y=160)         
        lbl_product_name=Label(product_frame,text="Name",font=("goudy old style",18),bg="white").place(x=30,y=200) 
        lbl_price=Label(product_frame,text="Price",font=("goudy old style",18),bg="white").place(x=30,y=240)
        lbl_mrp=Label(product_frame,text="MRP",font=("goudy old style",18),bg="white").place(x=30,y=280) 
        lbl_qty=Label(product_frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=30,y=320) 
        lbl_status=Label(product_frame,text="Status",font=("goudy old style",18),bg="white").place(x=30,y=360)  

        #===column2=====

        txt_date=Entry(product_frame,textvariable=self.var_date,font=("goudy old style",15),bg="lightyellow").place(x=180,y=40,width=200)

        txt_pid=Entry(product_frame,textvariable=self.var_hsn,font=("goudy old style",15),bg="lightyellow").place(x=180,y=80,width=200)

        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=180,y=120,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=180,y=160,width=200)
        cmb_sup. current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("goudy old style",15),bg='lightyellow').place(x=180,y=200,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("goudy old style",15),bg='lightyellow').place(x=180,y=240,width=200)
        txt_mrp=Entry(product_frame,textvariable=self.var_mrp,font=("goudy old style",15),bg="lightyellow").place(x=180,y=280,width=200)
        txt_qty=Entry(product_frame,textvariable= self.var_qty,font=("goudy old style",15),bg='lightyellow').place(x=180,y=320,width=200)

        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=180,y=360,width=200)
        cmb_status.current(0)


        #===buttons====
        btn_add=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
        # btn_prod_apmc=Button(product_frame,text="APMC Products",command=self.prod_apmc,font=("goudy old style",15),bg="white",cursor="hand2").place(x=10,y=450,width=200,height=20)

        #===searchFrame=====
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("goudy old style",12,""))
        SearchFrame.place(x=480,y=10,width=600,height=80)

        #===options===
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        #====Product Details===

        product_frame=Frame(self.root,bd=3,relief=RIDGE)
        product_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(product_frame,orient=VERTICAL)
        scrollx=Scrollbar(product_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(product_frame,columns=("date","pid","Category","Supplier","name","price","mrp","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("date",text="Date")
        self.ProductTable.heading("pid",text="P ID")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("mrp",text="MRP")
        self.ProductTable.heading("qty",text="Qty")
        self.ProductTable.heading("status",text="Status")
        self.ProductTable["show"]="headings"

        self.ProductTable.column("date",width=100)
        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("Category",width=100)
        self.ProductTable.column("Supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("mrp",width=90)
        self.ProductTable.column("qty",width=100)  
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()
        

#================================================================================

    def prod_apmc(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=prod_apmcClass(self.new_win)

    def fetch_cat_sup(self):
        self.cat_list.append("Select")
        self.sup_list.append("Select")
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
                    
            cur.execute("Select name from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_hsn.get()=="": #or self.var_sup.get()=="Select": #or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from products where Category=?",(self.var_hsn.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product ID is Alreary Assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into products (date,pid,Category,Supplier,name,price,mrp,qty,status) values(?,?,?,?,?,?,?,?,?)",(
                                        self.var_date.get(),
                                        self.var_hsn.get(),
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_mrp.get(),
                                        self.var_qty.get(),
                                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Succes","Product Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from products")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        #print(row)
        self.var_date.set(row[0])
        self.var_hsn.set(row[1])
        self.var_cat.set(row[2])
        self.var_sup.set(row[3])
        self.var_name.set(row[4])
        self.var_price.set(row[5])
        self.var_mrp.set(row[6])
        self.var_qty.set(row[7])
        self.var_status.set(row[8])


    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_hsn.get()=="": #or self.var_sup.get()=="Select": #or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from products where Category=?",(self.var_cat.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    cur.execute("Update products set date=?,Category=?,Supplier=?,name=?,price=?,mrp=?,qty=?,status=? where pid=?",(
                                        self.var_date.get(),
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_mrp.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_hsn.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Succes","Product Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_hsn.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                messagebox.showerror("Error","All Fields must be required",parent=self.root)
            else:
                cur.execute("Select * from products where pid=?",(self.var_hsn.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from products where pid=?",(self.var_hsn.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_date.set("")
        self.var_hsn.set("")
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_mrp.set("")                                       
        self.var_qty.set("")
        self.var_status.set("Select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input is Required",parent=self.root)
            else:
                cur.execute("Select * from products where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop()
