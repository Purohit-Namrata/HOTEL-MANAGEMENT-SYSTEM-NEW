from tkinter import *
from pymysql import *
from tkinter import messagebox


def add_customer():
    root1=Tk()
    root1.title("Add customer")
    e1=Entry(root1, "Customer's full name")
    e2=Entry(root1,"Contact number")
    e3=Entry(root1, "Identity proof(Aadhar number)")

    info1=el.getinfo()
    info2=e2.getinfo()
    info3=e3.getinfo()
    if (info1==None) or (info1==('[0-9]+')) :
        messagebox.showinfo("Error", "Please enter valid name")
    if ((info2==None) or (info2=='[a-z]+') or (len(info2)<10)):
        messagebox.showinfo("Error", "Please enter valid contact number")
    if(info3==None or (len(info3)<12) ):
        messagebox.showinfo("Error", "Please enter valid Aadhar number")
    
    btn1=Button(root1, text="Submit", fg='Black', bg='Light Grey')
    btn2=Button(root1, text="Exit", fg='Black', bg='Light Grey')

    e1.pack()
    e2.pack()
    btn1.pack()
    btn2.pack()
    root1.mainloop()

def checkin():
    pass

def checkout():
    pass

root=Tk()
root.title("Hotel Management System")
root.minsize(width=400,height=400)
root.geometry("600x500")
b1= Button(root,text="Add customer details", bg='Black', fg="Grey", command=add_customer)
#b2=Button(root, "Checkin", bg="Black", fg="Grey", command=checkin)
#b3=Button(root, "Checkout", bg="Black", fg="Grey", command=checkout)
b4=Button(root,text= "Exit",bg="Black",fg="Grey")
b1.pack(padx=20,pady=20)
#b2.pack(padx=20,pady=20)
#b3.pack(padx=20,pady=20)

root.mainloop()
