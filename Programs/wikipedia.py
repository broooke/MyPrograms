import requests
from tkinter import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
import time



#wik = Tk()
#wik.title("Random article from Wiki")
wiki=True
while wiki==True:
    try:
        url = "https://en.wikipedia.org/wiki/Special:Random"

        page = urlopen(url)

        html = page.read().decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")

        print(soup.title.string)
        ans = input("If you want to see this article, write 'y' else 'n'")
        if ans=='Y' or ans=='y':
            print('Article open! Wait five seconds!')
            time.sleep(5)
            webbrowser.open(url)
            wiki = False
        else:
            print("New article is generate")
            time.sleep(2)
    except:
        print("Check your internet connection.")

#lab_title = Label(text="Title", font=("ARIEL",15)).grid(row=0,column=0, padx=20,pady=10,sticky=W)
#lab1_title = Label(text="None", font=("ARIEL",15), width=50).grid(row=0,column=1)

#lab_status = Label(text="Status", font=("ARIEL",15)).grid(row=1,column=0,padx=20,pady=10,sticky=W)
#lab1_status = Label(text="None", font=("ARIEL",15), width=50).grid(row=1,column=1)
#gen()



#wik.mainloop()



