import threading
import win10toast

time = int(input("Enter the number of seconds: "))

def clock():
    title="""Alarm Clock"""
    message="""Time ran out {} seconds ago""".format(time)
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(title, message, duration=10, icon_path="covid-19.ico")

t = threading.Timer(time, clock) 
t.start()