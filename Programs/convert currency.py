from tkinter import *
from forex_python.converter import CurrencyRates

def convert():
    c = CurrencyRates()
    convert = c.convert(variable.get(),variable1.get(),int(amount.get()))
    cur.set(str(convert))


OPTIONS = [
"RUB",
"EUR",
"USD",
"JPY",
"CHF",
"GBP",
"AUD",
"CAD",
"SEK",
"BZR",
"INR",
"CNY",
] #etc

val = Tk()
val.title("Convertor currency")

cur = StringVar()
variable = StringVar(val)
variable.set(OPTIONS[0]) # default value
variable1 = StringVar(val)
variable1.set(OPTIONS[1])
amount  = StringVar()



ent = Entry(val,font=('arial', 20,'bold'), textvariable = cur).grid(row = 0, column = 0)
ent1 = Entry(val,font=('arial', 20,'bold'), textvariable = amount).grid(row = 4, column = 0)
btn = Button(val,padx=16,pady=16,bd=8,text='Convert', command = convert).grid(row=1,column=0)
men = OptionMenu(val, variable, *OPTIONS).grid(row=2, column = 0)
men1 = OptionMenu(val, variable1, *OPTIONS).grid(row=3, column = 0)



val.mainloop()


"""
c = CurrencyRates()
a = input("Enter the currency you want to convert from:").upper()
b = input("Enter the currency you want to convert:").upper()
amount = int(input("Enter the number of money you want to convert: "))
print(c.convert(a,b,amount))
"""