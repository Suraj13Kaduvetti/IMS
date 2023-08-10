from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class prod_apmcClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Developed By Ayush")
        self.root.config(bg="white")
        self.root.focus_force()

if __name__=="__main__":
    root=Tk()
    #root.attributes('-fullscreen',True)
    #root.resizable(False,False)
    obj=prod_apmcClass(root)
    root.mainloop()