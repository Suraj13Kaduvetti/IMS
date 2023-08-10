from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
import os
import email_pass
import smtplib #pip install smtplib                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             `                                                                                                               `
import time

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Project")
        self.root.geometry("450x650+500+60")
        self.root.config(bg="#fafafa")

        self.otp=''
        # #====images=====
        # self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        # self.lbl_image=Label(self.root,image=self.phone_image,bd=0).place(x=180,y=70,height=620)

        #====Login Frame======

        self.var_emp_id=StringVar()
        self.var_password=StringVar()

        Login_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Login_Frame.place(x=50,y=30,width=350,height=500)

        Frametitle=Label(Login_Frame,text="Login System",font=("Elephant",30,"bold"),bg="aliceblue",fg="navy").place(x=0,y=10,relwidth=1)

        lbl_emp_id=Label(Login_Frame,text="Employee ID",font=("Andalus",15),bg="#ECECEC",fg="#767171").place(x=50,y=100)
        txt_emp_id=Entry(Login_Frame,textvariable=self.var_emp_id,font=("times new roman",15),bg="lightyellow",fg="blue").place(x=50,y=140,width=180,height=30)

        lbl_password=Label(Login_Frame,text="Password",font=("Andalus",15),bg="#ECECEC",fg="#767171").place(x=50,y=200)
        txt_password=Entry(Login_Frame,textvariable=self.var_password,show="*",font=("times new roman",15),bg="lightyellow",fg="blue").place(x=50,y=240,width=180,height=30)

        #print(self.var_emp_id,self.var_password)

        btn_login=Button(Login_Frame,text=" Log In ",command=self.login,font=("Arial Rounded MT Bold",20,"bold"),bg="#00B0F0",activebackground="#00B0F0",fg="yellow",cursor="hand2").place(x=50,y=300,width=250,height=40)

        hr=Label(Login_Frame,bg="lightgreen").place(x=50,y=370,width=250,height=5)
        _or_=Label(Login_Frame,text="OR",font=("Helvetica",10,"bold"),bg="white",fg="lightgreen").place(x=160,y=357,height=30)

        lbl_forgot_pass=Label(Login_Frame,text="Forgot Password\n↓Click Below↓",font=("Impact",15),bg="#FFFF00",fg="skyblue").place(x=50,y=390,width=250,height=50)
        btn_forget_pass=Button(Login_Frame,text=" Forget Password ? ",command=self.for_pass_win,font=("Comic Sams MS",15,"bold"),bg="white",fg="aquamarine",bd=0,cursor="hand2",activebackground="white",activeforeground="aquamarine").place(x=65,y=450,width=220,height=20)

        #===Register Frame=====

        Sign_Up_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Sign_Up_Frame.place(x=50,y=550,width=350,height=70)

        lbl_register_info=Label(Sign_Up_Frame,text=" ↓Don't have an Account??↓ ",font=("Candara",15,"bold"),bg="azure",fg="teal").place(x=55,y=5)
        btn_sign_up=Button(Sign_Up_Frame,text=" ..Sign Up.. ",command=self.sign_up,font=("",15,"bold"),bg="white",fg="lime",cursor="hand2",bd=0,activebackground="white",activeforeground="lime").place(x=90,y=40,width=150,height=20)

    #     #====Animation Images=======
    #
    #     self.im1=ImageTk.PhotoImage(file="images/im1.png")
    #     self.im2=ImageTk.PhotoImage(file="images/im2.png")
    #     self.im3=ImageTk.PhotoImage(file="images/im3.png")
    #
    #     self.lbl_change_image=Label(self.root,bg="white")
    #     self.lbl_change_image.place(x=347,y=177,width=240,height=428)
    #
    #     self.animate_image()
    #     #self.send_email('sppr.8448@gmail.com')
    #
    # def animate_image(self):
    #     self.im0=self.im1
    #     self.im1=self.im2
    #     self.im2=self.im3
    #     self.im3=self.im0
    #     self.lbl_change_image.config(image=self.im0)
    #     self.lbl_change_image.after(2000,self.animate_image)

    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="" or self.var_password.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.var_emp_id.get(),self.var_password.get()))
                employee=cur.fetchone()
                if employee==None:
                    messagebox.showwarning("Warning","Invalid Employee ID or Password",parent=self.root)
                else:
                    #print(employee)
                    if employee[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        '''if self.var_emp_id.get()=="" or self.var_password.get()=="":
            messagebox.showerror("Error","All Fields are Required!!!")
        elif self.var_emp_id.get()!="Ayush" or self.var_password.get()!="19875":
                messagebox.showwarning("Warning","Invalid Username or Password\nTry Again with Correct Credentials")
        else:
            messagebox.showinfo("Information",f"Welcome : {self.var_emp_id.get()}\n Your PAssword is {self.var_password.get()}")'''

    def for_pass_win(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID is Mandatory!!!",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.var_emp_id.get(),))
                email=cur.fetchone()
                if email[0]==None:
                    messagebox.showwarning("Warning","Invalid Employee ID\nTry Again",parent=self.root)
                else:
                    #print(email[0])
                    #====Forget Password Window=========
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_con_pass=StringVar()
                    #call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error Try Again",parent=self.root)
                    else:
                        self.forget_password_window=Toplevel(self.root)
                        self.forget_password_window.title("RESET PASSOWRD")
                        self.forget_password_window.geometry("400x400+500+100")
                        self.forget_password_window.focus_force()
                        #======labels====
                        forpasstitle=Label(self.forget_password_window,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        
                        lbl_reset=Label(self.forget_password_window,text="Enter the OTP sent on the Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_password_window,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        
                        self.btn_reset=Button(self.forget_password_window,text="SUBMIT/RESET",command=self.validate_otp,font=("times new roman",10),bg="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)
                        #self.btn_reset.after(500,self.send_email('sppr.8448@gmail.com'))
                        
                        lbl_new_pass=Label(self.forget_password_window,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_password_window,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
    
                        lbl_con_pass=Label(self.forget_password_window,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                        txt_con_pass=Entry(self.forget_password_window,textvariable=self.var_con_pass,show="*",font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)

                        self.btn_update=Button(self.forget_password_window,text="UPDATE",command=self.update_pass,font=("times new roman",15),state=DISABLED,bg="forestgreen",fg="azure")
                        self.btn_update.place(x=150,y=300,width=100,height=50)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        #messagebox.showinfo("Forgot Password","You have selected Forgot Password")

    def sign_up(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            self.forget_password_window=Toplevel(self.root)
            self.forget_password_window.title("SIGN UP")
            self.forget_password_window.geometry("1000x500+100+60")
            self.forget_password_window.config(bg="white")
            self.forget_password_window.focus_force()
            #===Employee Entry=====
            self.var_new_emp_id=StringVar()
            self.var_new_gender=StringVar()
            self.var_new_contact=StringVar()
            self.var_new_name=StringVar()
            self.var_new_dob=StringVar()
            self.var_new_doj=StringVar()
            self.var_new_email=StringVar()
            self.var_new_pass=StringVar()
            self.var_new_utype=StringVar()
            self.var_new_salary=StringVar()
            self.var_new_address=StringVar()

            title=Label(self.forget_password_window,text="Employee Entry Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=10,y=10,width=1000)

            #====content=======

            #===row1====

            lbl_new_empid=Label(self.forget_password_window,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=50)
            lbl_new_name=Label(self.forget_password_window,text="Name",font=("goudy old style",15),bg="white").place(x=500,y=50)

            txt_new_empid=Entry(self.forget_password_window,textvariable=self.var_new_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=50,width=250)
            txt_new_name=Entry(self.forget_password_window,textvariable=self.var_new_name,font=("goudy old style",15),bg="lightyellow").place(x=600,y=50,width=250)
            
            #===row2====

            lbl_new_contact=Label(self.forget_password_window,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=100)
            lbl_new_email=Label(self.forget_password_window,text="Email",font=("goudy old style",15),bg="white").place(x=500,y=100)

            txt_new_contact=Entry(self.forget_password_window,textvariable=self.var_new_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=100,width=200)
            txt_new_email=Entry(self.forget_password_window,textvariable=self.var_new_email,font=("goudy old style",15),bg="lightyellow").place(x=600,y=100,width=200)

            #===row3===

            lbl_new_dob=Label(self.forget_password_window,text="D.O.B",font=("goudy old style",15),bg="white").place(x=50,y=150)
            lbl_new_doj=Label(self.forget_password_window,text="D.O.J",font=("goudy old style",15),bg="white").place(x=500,y=150)

            txt_new_dob=Entry(self.forget_password_window,textvariable=self.var_new_dob,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=200)
            txt_new_doj=Entry(self.forget_password_window,textvariable=self.var_new_doj,font=("goudy old style",15),bg="lightyellow").place(x=600,y=150,width=200)

            #===row4===

            lbl_new_gender=Label(self.forget_password_window,text="Gender",font=("goudy old style",15),bg="white").place(x=50,y=200)
            lbl_new_utype=Label(self.forget_password_window,text="User Type",font=("goudy old style",15),bg="white").place(x=500,y=200)

            cmb_new_gender=ttk.Combobox(self.forget_password_window,textvariable=self.var_new_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
            cmb_new_gender.place(x=150,y=200,width=200)
            cmb_new_gender.current(0)
            cmb_new_utype=ttk.Combobox(self.forget_password_window,textvariable=self.var_new_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
            cmb_new_utype.place(x=600,y=200,width=200)
            cmb_new_utype.current(0)
            

            #===row5====

            lbl_new_salary=Label(self.forget_password_window,text="Salary",font=("goudy old style",15),bg="white").place(x=50,y=250)
            lbl_new_pass=Label(self.forget_password_window,text="Password",font=("goudy old style",15),bg="white").place(x=500,y=250)

            txt_new_pass=Entry(self.forget_password_window,textvariable=self.var_new_pass,font=("goudy old style",15),bg="lightyellow").place(x=150,y=250,width=200)
            txt_new_salary=Entry(self.forget_password_window,textvariable=self.var_new_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=250,width=200)            

            #===row6====

            lbl_new_address=Label(self.forget_password_window,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=300)

            self.new_txt_address=Text(self.forget_password_window,font=("goudy old style",15),bg="lightyellow")
            self.new_txt_address.place(x=150,y=300,width=300,height=100)

            #===buttons====

            btn_new_add=Button(self.forget_password_window,text="Add User",command=self.new_add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=50,y=450,width=200,height=28)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    def new_add(self):
                con=sqlite3.connect(database=r'ims.db')
                cur=con.cursor()
                try:
                    if self.var_new_emp_id.get()=="": #or self.var_name.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_contact.get()=="" or self.var_dob.get()=="" or self.var_doj.get()=="" or self.var_pass.get()=="" or self.var_utype.get()=="" or self.var_address.get()=="" or self.var_salary.get()=="":
                        messagebox.showerror("Error","All Fields must be required",parent=self.forget_password_window)
                    else:
                        cur.execute("Select * from employee where eid=?",(self.var_new_emp_id.get(),))
                        row=cur.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","This Employee ID is Alreary Assigned, try different",parent=self.root)
                        else:
                            cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                self.var_new_emp_id.get(),
                                                self.var_new_name.get(),
                                                self.var_new_email.get(),
                                                self.var_new_gender.get(),
                                                self.var_new_contact.get(), 
                                                self.var_new_dob.get(),
                                                self.var_new_doj.get(),
                                                self.var_new_salary.get(),                          
                                                self.var_new_utype.get(),
                                                self.new_txt_address.get('1.0',END),
                                                self.var_new_pass.get(),
                                                #self.var_address.get()
                            ))
                            con.commit()
                            messagebox.showinfo("Succes","Employee Added Successfully",parent=self.forget_password_window)
                        messagebox.showinfo("Success","Sign Up Successful")
                        self.forget_password_window.destroy()
                except Exception as ex:
                    messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.forget_password_window)

    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%M%H%S"))
        #print(self.otp)
        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir/Madam\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regard,\nIMS Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 'Success'
        else:
            return 'Failure'

    def update_pass(self):
        if self.var_new_pass.get()=="" or self.var_con_pass.get()=="":
            messagebox.showerror("Error","Password is Required",parent=self.forget_password_window)
        elif self.var_new_pass.get()!=self.var_con_pass.get():
            messagebox.showerror("Error","New Password & Confirm Password should be same",parent=self.forget_password_window)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee set pass=? where eid=?",(self.var_new_pass.get(),self.var_emp_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password Canged Successfully")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP\tTry Again",parent=self.forget_password_window)
        
#if __name__=="__main__":
root=Tk()
obj=Login_System(root)
root.mainloop()
