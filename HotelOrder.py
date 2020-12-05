from tkinter import *
from tkinter import ttk

#--------------------Method for Printing The Receipt-----------------------------------------
def print():
    tott = float(totText.get())
    top = Toplevel()
    top.geometry("300x300")

    top.config(bg="white")
    l = Label(top, text='---------RECIEPT----------')
    l.pack()
    l.config(bg="white")
    heading = Label(top, text='\tItem\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(bg="white")

    for child in listBox.get_children():
        item = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty = float(listBox.item(child, 'values')[2])
        tot = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t{price}\t{qty}\t{tot}')
        item1.config(bg="white")
        item1.pack()

    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()

#----------------------This is the method for showing the items, price quantity and total-------------------
def show():
    tot = 0
    if (var1.get()):
        price = int(e1.get())
        qty = int(e6.get())
        tot = int(price * qty)
        tempList = [['Tea', e1.get(), e6.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var2.get()):
        price = int(e2.get())
        qty = int(e7.get())
        tot = int(price * qty)
        tempList = [['Chapati', e2.get(), e7.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var3.get()):
        price = int(e3.get())
        qty = int(e8.get())
        tot = int(price * qty)
        tempList = [['Chicken Fry', e3.get(), e8.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var4.get()):
        price = int(e4.get())
        qty = int(e9.get())
        tot = int(price * qty)
        tempList = [['Ugali Beef', e4.get(), e9.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var5.get()):
        price = int(e5.get())
        qty = int(e10.get())
        tot = int(price * qty)
        tempList = [['Fish Fried Rice', e5.get(), e10.get(), tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3])
    totText.set(sum1)
#----------------This Method is for payment it calculates the total amount then gives the balance------------
def pay():
    totall=float(tot.cget("text"))
    pay=float(e11.get())
    bal= pay-totall
    balText.set(bal)
#----------------This method cancels the order incase the customer does not have enough cash or there is no food-----
def cancel():
    totText.set("")
    balText.set("")
   



root = Tk()
root.title("Hotel Order System")
root.geometry("1000x600")
global e1
global e2
global e3
global e4
global totText
global balText

totText = StringVar()
balText = IntVar()

Label(root, text="Hotel Order System", font="arial 22 bold", bg="white").place(x=200, y=5)
#----This are the variables that are used to place the values--------
var1 = IntVar()
Checkbutton(root, text="Tea", font="times 12", variable=var1).place(x=10, y=50)

var2 = IntVar()
Checkbutton(root, text="Chapati", font="times 12", variable=var2).place(x=10, y=80)

var3 = IntVar()
Checkbutton(root, text="Chicken Fry", font="times 12", variable=var3).place(x=10, y=110)

var4 = IntVar()
Checkbutton(root, text="Ugali Beef", font="times 12", variable=var4).place(x=10, y=140)

var5 = IntVar()
Checkbutton(root, text=" Fish Fried Rice  ", font="times 12", variable=var5).place(x=10, y=170)
Label(root, text="Total",font="times 12 bold",).place(x=550, y=10)
Label(root, text="Pay",font="times 12 bold",).place(x=550, y=50)
Label(root, text="Balance",font="times 12 bold",).place(x=550, y=90)

#------This are the boxes for showing values entered by the user-------
e1 = Entry(root)
e1.place(x=140, y=50)

e2 = Entry(root)
e2.place(x=140, y=80)

e3 = Entry(root)
e3.place(x=140, y=110)

e4 = Entry(root)
e4.place(x=140, y=140)

e5 = Entry(root)
e5.place(x=140, y=170)

e6 = Entry(root)
e6.place(x=300, y=50)

e7 = Entry(root)
e7.place(x=300, y=80)

e8 = Entry(root)
e8.place(x=300, y=110)

e9 = Entry(root)
e9.place(x=300, y=140)

e10 = Entry(root)
e10.place(x=300, y=170)

e11 = Entry(root)
e11.place(x=650, y=50)

tot = Label(root, text="", font="arial 22 bold", textvariable=totText)
tot.place(x=650, y=10)
balance=Label(root,text="",font="arial 22 bold",textvariable=balText).place(x=650,y=80)
#------This are the buttons which carryout the necessary commands------
Button(root, text="Add", command=show, height=3, width=13,font="times 12 bold",bg="orange").place(x=10, y=220)
Button(root,text="Cancel",command= cancel,height=3,width=13,font="times 12 bold",bg="orange").place(x=180,y=220)
Button(root, text="Print", command=print, height=3, width=13,font="times 12 bold",bg="orange").place(x=350, y=220)
Button(root, text="Pay", command=pay, height=3, width=13,font="times 12 bold",bg="orange").place(x=550, y=220)

#-----------Menu Section---------
label1=Label(root,text="Menu",font=" times 20 bold")
label1.place(x=800,y=70)
label2=Label(root,text="Tea                          kshs     30 ", font="times 12")
label2.place(x=750,y=120)
label3=Label(root,text="Chapati                    kshs     20 ", font="times 12")
label3.place(x=750,y=150)
label4=Label(root,text="Chicken Fry             kshs   120 ", font="times 12")
label4.place(x=750,y=180)
label5=Label(root,text="Ugali Beef                kshs   100 ", font="times 12")
label5.place(x=750,y=210)
label6=Label(root,text="Fish Fried Rice         kshs  160 ", font="times 12")
label6.place(x=750,y=240)

#-----This is the table where the items are displayed before being printed in the receipt-----
cols = ('item', 'price', 'qty', 'total')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=350)

root.mainloop()