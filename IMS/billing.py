from tkinter import *
from turtle import width
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import time
import os
import tempfile
#from employee import employeeClass
#from Productplier import ProductplierClass
#from category import categoryClass
#from products import productClass
#from sales import salesClass
class billClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1370x800+0+0")
        #self.root.geometry("1920x1000+0+0")
        #self.root.attributes()
        #screen_width = self.root.winfo_screenwidth()
        #screen_height = self.root.winfo_screenheight()
        #self.root.geometry("screen_widthxscreen_height")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0
        #===title=====
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",command=self.log_out,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)
        
        #===clock=====
        self.lbl_clock=Label(self.root,text="Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Product Frame Hold========================
        Product_Frame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Product_Frame1.place(x=6,y=110,width=410,height=570)

        PTitle=Label(Product_Frame1,text="All Products",font=("goudy old style",20,"bold"),bg="forestgreen",fg="white").pack(side=TOP,fill=X)

        #===Product Search Frame========================
        #===Product Frames=====
        self.var_search=StringVar()

        Product_Frame2=Frame(Product_Frame1,bd=2,relief=RIDGE,bg="white")
        Product_Frame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(Product_Frame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="aliceblue",fg="yellowgreen").place(x=2,y=5)
        
        lbl_search=Label(Product_Frame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search=Entry(Product_Frame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=135,y=47,width=150,height=22)
        btn_search=Button(Product_Frame2,text="Search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=100,height=25)
        btn_show_all=Button(Product_Frame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=290,y=10,width=100,height=25)

        #===Product Details Frame========================
        Product_Frame3=Frame(Product_Frame1,bd=3,relief=RIDGE)
        Product_Frame3.place(x=2,y=150,width=398,height=385)

        scrolly=Scrollbar(Product_Frame3,orient=VERTICAL)
        scrollx=Scrollbar(Product_Frame3,orient=HORIZONTAL)

        #===Product Details========

        self.Product_Table=ttk.Treeview(Product_Frame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Product_Table.xview)
        scrolly.config(command=self.Product_Table.yview)
        #self.var_date.set("")
        self.Product_Table.heading("pid",text="PID")
        self.Product_Table.heading("name",text="Name")
        self.Product_Table.heading("price",text="Price")
        self.Product_Table.heading("qty",text="QTY")
        self.Product_Table.heading("status",text="Status")
        self.Product_Table["show"]="headings"

        self.Product_Table.pack(fill=BOTH,expand=1)

        self.Product_Table.column("pid",width=80)
        self.Product_Table.column("name",width=90)
        self.Product_Table.column("price",width=100)
        self.Product_Table.column("qty",width=100)
        self.Product_Table.column("status",width=100)
        self.Product_Table.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(Product_Frame1,text="Note : 'Enter 0 QTY to Remove Product from Cart'",font=("times new roman",13,"bold"),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #====Customer Frame=========
        self.var_cust_name=StringVar()
        self.var_contact=StringVar()
        Customer_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Customer_Frame.place(x=420,y=110,width=530,height=70)

        CTitle=Label(Customer_Frame,text="Customer Details",font=("goudy old style",15,"bold"),bg="lightgray").pack(side=TOP,fill=X)
        lbl_name=Label(Customer_Frame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name=Entry(Customer_Frame,textvariable=self.var_cust_name,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180,height=22)
        lbl_contact=Label(Customer_Frame,text="Contact",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact=Entry(Customer_Frame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=350,y=35,width=160,height=22)

        #===Cal Cart Frame========================
        Cal_Cart_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

        # #===Calculator Frame========================
        # self.var_cal_input=StringVar()
        #
        # Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        # Cal_Frame.place(x=3,y=10,width=268,height=340)
        #
        # txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        # txt_cal_input.grid(row=0,columnspan=4)
        #
        # #===row1=====
        # btn_7=Button(Cal_Frame,text=7,font=("arial",15,"bold"),command=lambda:self.get_input(7),bd=5,width=4,pady=6,cursor="hand2").grid(row=1,column=0)
        # btn_8=Button(Cal_Frame,text=8,font=("arial",15,"bold"),command=lambda:self.get_input(8),bd=5,width=4,pady=6,cursor="hand2").grid(row=1,column=1)
        # btn_9=Button(Cal_Frame,text=9,font=("arial",15,"bold"),command=lambda:self.get_input(9),bd=5,width=4,pady=6,cursor="hand2").grid(row=1,column=2)
        # btn_div=Button(Cal_Frame,text="÷",font=("arial",15,"bold"),command=lambda:self.get_input('/'),bd=5,width=4,pady=6,cursor="hand2").grid(row=1,column=3)
        #
        #
        # #===row2=====
        # btn_4=Button(Cal_Frame,text=4,font=("arial",15,"bold"),command=lambda:self.get_input(4),bd=5,width=4,pady=6,cursor="hand2").grid(row=2,column=0)
        # btn_5=Button(Cal_Frame,text=5,font=("arial",15,"bold"),command=lambda:self.get_input(5),bd=5,width=4,pady=6,cursor="hand2").grid(row=2,column=1)
        # btn_6=Button(Cal_Frame,text=6,font=("arial",15,"bold"),command=lambda:self.get_input(6),bd=5,width=4,pady=6,cursor="hand2").grid(row=2,column=2)
        # btn_sub=Button(Cal_Frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input('-'),bd=5,width=4,pady=6,cursor="hand2").grid(row=2,column=3)
        #
        # #===row3======
        # btn_1=Button(Cal_Frame,text=1,font=("arial",15,"bold"),command=lambda:self.get_input(1),bd=5,width=4,pady=6,cursor="hand2").grid(row=3,column=0)
        # btn_2=Button(Cal_Frame,text=2,font=("arial",15,"bold"),command=lambda:self.get_input(2),bd=5,width=4,pady=6,cursor="hand2").grid(row=3,column=1)
        # btn_3=Button(Cal_Frame,text=3,font=("arial",15,"bold"),command=lambda:self.get_input(3),bd=5,width=4,pady=6,cursor="hand2").grid(row=3,column=2)
        # btn_mul=Button(Cal_Frame,text="x",font=("arial",15,"bold"),command=lambda:self.get_input('*'),bd=5,width=4,pady=6,cursor="hand2").grid(row=3,column=3)
        #
        # #===row4======
        # btn_point=Button(Cal_Frame,text=".",font=("arial",15,"bold"),command=lambda:self.get_input('.'),bd=5,width=4,pady=6,cursor="hand2").grid(row=4,column=0)
        # btn_0=Button(Cal_Frame,text=0,font=("arial",15,"bold"),command=lambda:self.get_input(0),bd=5,width=4,pady=6,cursor="hand2").grid(row=4,column=1)
        # btn_percent=Button(Cal_Frame,text="%",font=("arial",15,"bold"),command=self.calPercent,bd=5,width=4,pady=6,cursor="hand2").grid(row=4,column=2)
        # btn_add=Button(Cal_Frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input('+'),bd=5,width=4,pady=6,cursor="hand2").grid(row=4,column=3)
        #
        #
        # #===row5====
        # btn_c=Button(Cal_Frame,text="C",font=("arial",15,"bold"),command=self.clear_cal,bd=5,width=4,pady=6,cursor="hand2").grid(row=5,column=0)
        # btn_backcheck=Button(Cal_Frame,text="<-Ch",font=("arial",15,"bold"),bd=5,width=4,pady=6,cursor="hand2").grid(row=5,column=1)
        # btn_frontcheck=Button(Cal_Frame,text="Ch->",font=("arial",15,"bold"),bd=5,width=4,pady=6,cursor="hand2").grid(row=5,column=2)
        # btn_equal=Button(Cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,bd=5,width=4,pady=6,cursor="hand2").grid(row=5,column=3)

        #===Cart Frame========================
        Cart_Frame=Frame(Cal_Cart_Frame,bd=2,relief=RIDGE)
        Cart_Frame.place(x=10,y=10,width=500,height=342)
        self.CartTitle=Label(Cart_Frame,text="Cart \tTotal Products : [ 0 ]",font=("goudy old style",15),bg="lightgray")
        self.CartTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)

        #===Product Details========

        self.Cart_Table=ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Cart_Table.xview)
        scrolly.config(command=self.Cart_Table.yview)
        #self.var_date.set("")
        self.Cart_Table.heading("pid",text="PID")
        self.Cart_Table.heading("name",text="Name")
        self.Cart_Table.heading("price",text="Price")
        self.Cart_Table.heading("qty",text="QTY")
        #self.Cart_Table.heading("status",text="Status")
        self.Cart_Table["show"]="headings"

        self.Cart_Table.pack(fill=BOTH,expand=1)

        self.Cart_Table.column("pid",width=40)
        self.Cart_Table.column("name",width=100)
        self.Cart_Table.column("price",width=90)
        self.Cart_Table.column("qty",width=90)
        #self.Cart_Table.column("status",width=90)
        self.Cart_Table.pack(fill=BOTH,expand=1)
        self.Cart_Table.bind("<ButtonRelease-1>",self.get_cart_data)

        #===ADD Cart Widgets Frame========================
        self.var_pid=StringVar()
        self.var_prod_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_dis_prct=StringVar()

        Add_Cart_Widgets_Frame=Frame(self.root,bd=6,relief=RIDGE,bg="white")
        Add_Cart_Widgets_Frame.place(x=420,y=550,width=530,height=110)

        lbl_P_Name=Label(Add_Cart_Widgets_Frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_P_Name=Entry(Add_Cart_Widgets_Frame,textvariable=self.var_prod_name,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_P_Price=Label(Add_Cart_Widgets_Frame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=210,y=5)
        txt_P_Pice=Entry(Add_Cart_Widgets_Frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=210,y=35,width=150,height=22)

        lbl_P_Qty=Label(Add_Cart_Widgets_Frame,text="Quantity",font=("times new roman",15),bg="white").place(x=370,y=5)
        txt_P_Qty=Entry(Add_Cart_Widgets_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=370,y=35,width=150,height=22)

        self.lbl_inStock=Label(Add_Cart_Widgets_Frame,text="In Stock",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Add_Cart_Widgets_Frame,text="Clear",command=self.clear_cart,font=("goudy old style",15,"bold"),bg="lightgray",cursor="hand2").place(x=160,y=70,width=150,height=30)
        btn_add_cart=Button(Add_Cart_Widgets_Frame,text="Add | Update Cart",command=self.add_update_cart,font=("goudy old style",15,"bold"),bg="aliceblue",cursor="hand2").place(x=320,y=70,width=180,height=30)

        #======================billing area===========

        Bill_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Bill_Frame.place(x=953,y=110,width=420,height=410)
        BTitle=Label(Bill_Frame,text="Customer Bills Area",font=("times new roman",15,"bold"),bg="skyblue",fg="white").pack(side=TOP,fill=X)

        scrolly=Scrollbar(Bill_Frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area=Text(Bill_Frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

#======================Billing Buttons==================
        Bill_Menu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Bill_Menu_Frame.place(x=953,y=520,width=410,height=140)

        self.lbl_amt=Label(Bill_Menu_Frame,text="Bill Amount\n[ 0 ]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amt.place(x=2,y=5,width=160,height=70)

        self.lbl_dis=Label(Bill_Menu_Frame,text="Discount\n         %",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_dis.place(x=165,y=5,width=80,height=70)

        self.dis_prct=Entry(Bill_Menu_Frame,textvariable=self.var_dis_prct,font=("times new roman",15),bg="lightyellow")
        self.dis_prct.place(x=185,y=40,width=30,height=20)

        self.lbl_net_pay=Label(Bill_Menu_Frame,text="Net Pay\n[ 0 ]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)

        btn_print=Button(Bill_Menu_Frame,command=self.print_bill,text="Print",font=("goudy old style",15,"bold"),bg="lightgreen",fg="navy",cursor="hand2")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(Bill_Menu_Frame,text="Clear All",command=self.clear_all_bill,font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(Bill_Menu_Frame,text="Generate/Save Bill",command=self.generate_bill,font=("goudy old style",15,"bold"),bg="#009688",fg="white",cursor="hand2")
        btn_generate.place(x=246,y=80,width=160,height=50)

        #=================Foooter=================
        footer=Label(self.root,text="IMS Inventory Management System",font=("times new roman",10),bg="lightgreen",fg="maroon",activebackground="#4d636d",activeforeground="white",bd=0,cursor="hand2")
        footer.pack(side=BOTTOM,fill=X)

        self.show()
        self.update_date_time()
        
#=====All Functions===============
    # def get_input(self,num):
    #     xnum=self.var_cal_input.get()+str(num)
    #     self.var_cal_input.set(xnum)
    #
    # def clear_cal(self):
    #     self.var_cal_input.set('')
    #
    # def perform_cal(self):
    #     result=self.var_cal_input.get()
    #     self.var_cal_input.set(eval(result))
    #
    # def calPercent(self,num):
    #     per=self.var_cal_input.get()+str(num)/100*self.var_cal_input.get()+str(num)
    #     self.var_cal_input.set(eval(per))
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid,name,mrp,qty,status from products where status='Active'")
            rows=cur.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
                self.Product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search Input is Required",parent=self.root)
            else:
                cur.execute("Select pid,name,mrp,qty,status from products where name LIKE '%"+self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Product_Table.delete(*self.Product_Table.get_children())
                    for row in rows:
                        self.Product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.Product_Table.focus()
        content=(self.Product_Table.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_prod_name.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')

    def get_cart_data(self,ev):
        f=self.Cart_Table.focus()
        content=(self.Cart_Table.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_prod_name.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get()=="":
            messagebox.showerror("Error","Please Select Product from the list",paren=self.root)
        elif self.var_qty.get()=="":
            messagebox.showerror("Error","Quantity is Required",parent=self.root)
        elif (int(self.var_qty.get()) > int(self.var_stock.get())):
            self.dif=int((int(self.var_qty.get())-int(self.var_stock.get())))
            messagebox.showerror("Error",f"Quantity Less By {str(self.dif)}",parent=self.root)
        else:
            price_cal=int(self.var_qty.get())*float(self.var_price.get())
            price_cal=float(price_cal)
            #price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_prod_name.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
            #======update_cart=========
            present='no'
            _index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    #print(self.var_pid)
                    present='yes'
                    break
                _index_+=1
            if present=='yes':
                op=messagebox.askyesno("Confirm","Product already present\n Do you want to Update | Remove from the Cart List",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(_index_)
                    else:
                        self.cart_list[_index_][2]=price_cal #price
                        self.cart_list[_index_][3]=self.var_qty.get() #qty
            else:
                self.cart_list.append(cart_data)
            
            self.show_cart()
            self.bill_updates()

    def bill_updates(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        self.dis=float(self.dis_prct.get())
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
        self.discount=float((self.bill_amt*self.dis)/100)
        self.net_pay=self.bill_amt-self.discount
        self.lbl_amt.config(text=f"Bill Amount(₹)\n[{str(self.bill_amt)}]")
        self.lbl_net_pay.config(text=f"Net Amount(₹)\n[{str(self.net_pay)}]")
        self.CartTitle.config(text=f"Cart \t Total Products : [{str(len(self.cart_list))}]")

    def show_cart(self):
        try:
            #for len(self.cart_list)
            self.Cart_Table.delete(*self.Cart_Table.get_children())
            for row in self.cart_list:
                self.Cart_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def generate_bill(self):
        if self.var_cust_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details Required",parent=self.root)
        elif len((self.cart_list))<=0:
            messagebox.showerror("Error","Please Add Product to the Cart",parent=self.root)
        else:
            #=======Bill Top========
            self.bill_top()
            #=====Bill Middle=======
            self.bill_middle()
            #=====Bill Bottom========
            self.bill_bottom()
            fp=open(f'bill/{str(self.invoice)}.txt','w',encoding='utf-8')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved','Bill has beed Generated/Saved in Backend',parent=self.root)
            self.chk_print=1

    def bill_top(self):
        self.invoice=str(time.strftime("%H%M%S"))#+#" "+" "+str(time.strftime("%d/%m/%Y"))
        #print(invoice)
        bill_top_temp=f''' 
        \t\tXYZ-Inventory
      Phone No. 9876xxxx , Mumbai-487552
      Mob No. 9848xxxx
    \t  GST No.  : {"2755xx56498"}
    \t  FASI No. : {"654198x949849"}
{str("="*48)}
    Bill No. : {str(self.invoice)}\t\t       Date: {str(time.strftime("%d/%m/%Y"))}
    Customer Name: {self.var_cust_name.get()}
    Contact No. : {self.var_contact.get()}
{str("="*48)}
    Product Name\t\t\t\tQTY\tPrice
{str("="*48)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status="Inactive"
                if int(row[3])!=int(row[4]):
                    status="Active"
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\t(₹)"+price)
                #====update qty in product table=======
                cur.execute('Update products set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*48)}
    Bill Amount\t\t\t\t(₹){self.bill_amt}
    Discount\t\t\t\t(₹){self.discount}
    Net Amount\t\t\t\t(₹){self.net_pay}
    \n\n\n\n\n  Customer Sign
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_prod_name.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock [0]")
        self.var_stock.set('')

    def clear_all_bill(self):
        del self.cart_list[:]
        self.var_cust_name.set('')
        self.var_contact.set('')
        self.var_dis_prct.set('')
        self.txt_bill_area.delete('1.0',END)
        self.lbl_amt.config(text=f"Bill Amount(₹)\n[]0")
        self.lbl_net_pay.config(text=f"Net Amount(₹)\n[0]")
        self.CartTitle.config(text=f"Cart \t Total Products : [0]")
        self.var_search.set('')
        self.chk_print=0
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        _time_=time.strftime("%I:%M:%S")
        _date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date : {str(_date_)}\t\t Time :{str(_time_)}")
        self.lbl_clock.after(1000,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while Printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w',encoding='utf-8').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print","PLease generate bill first to print the reciept",parent=self.root)

    def log_out(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj=billClass(root)
    root.mainloop()
    #widthsrc = root.winfo_screenwidth()
    #heightsrc = root.winfo_screenheight()
    #print(widthsrc,heightsrc)
