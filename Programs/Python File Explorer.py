# Python program to create  
# a file explorer in Tkinter 
   
# import all components 
# from the tkinter library 
from tkinter import *
   
# import filedialog module 
from tkinter import filedialog 
import shutil
   
# Function for opening the  
# file explorer window 

def fileopen():
    fd = filedialog.askopenfilename(title = "Select file")

    path.set(fd)

def copy():
    src = path.get()
    print(src)
    des = path1.get()
    shutil.copy(src, des)

window = Tk() 
window.title('File Explorer') 
window.geometry("500x500")

path = StringVar()
path1 = StringVar()

ent = Entry(window,textvariable = path, width = 80, fg = "blue").grid(row = 1)
btn = Button(window,padx=16,pady=16,bd=8,text='Browse search', command = fileopen).grid(row = 2)
btn1 = Button(window,padx=16,pady=16,bd=8,text='Copy', command = copy).grid(row = 3)
ent2 = Entry(window, textvariable = path1, width = 80, fg = "blue").grid(row=4)


window.mainloop() 