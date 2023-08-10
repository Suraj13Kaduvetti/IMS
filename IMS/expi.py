'''def calPercent(num,integer = False):
    per=num/100

    if integer:
        return int(per)
    return per

print(calPercent(50))'''

#make product apmc like employee
#====================
#billing needs new additions like extra deep details
#===========================
#billing needs discount editor
#fsi number and gstin number display on bill
'''
sr No	item name	rate	qty	amount
1				
2				
3				
4				
5				
6				
7				
8				
9				
10				
11				
12				
13				
14				
15				
16				
17				
18				
19				
20				
21				

'''
#set alarm for those customers whose delivery time is given
#create a alphanumeric bill number


'''
#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("650x250")

#Get the current screen width and height
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#Print the screen size
print("Screen width:", screen_width)
print("Screen height:", screen_height)

win.mainloop()'''

from tkinter import *
  
# toplevel window
root = Tk()
  
# Method to make Button(Widget) invisible from toplevel
  
  
def hide_button(widget):
    # This will remove the widget from toplevel
    widget.pack_forget()
  
  
# Method to make Button(widget) visible
def show_button(widget):
    # This will recover the widget from toplevel
    widget.pack(side=RIGHT,fill=Y)
  
  
# Button widgets
B1 = Button(root, text="Button 1")
B1.pack(side=TOP,fill=X)
  
  
# See, in command hide_button() function is passed to hide Button B1
B2 = Button(root, text="Button 2", command=lambda: hide_button(B1))
B2.pack(side=LEFT,fill=Y)
  
# In command show_button() function is passed to recover Button B1
B3 = Button(root, text="Button 3", command=lambda: show_button(B1))
B3.pack(side=BOTTOM,fill=X)
  
root.mainloop()
