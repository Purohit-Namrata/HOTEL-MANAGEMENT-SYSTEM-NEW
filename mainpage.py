from tkinter import *
import re
from tkinter import messagebox

def add_customer():
    def submit_details():
        info1 = e1.get()
        info2 = e2.get()
        info3 = e3.get()

        if not re.match(r"^[A-Za-z\s]+$", info1):
            messagebox.showinfo("Error", "Please enter a valid name")
            return
        if not re.match(r"^[0-9]{10}$", info2):
            messagebox.showinfo("Error", "Please enter a valid contact number")
            return
        if not re.match(r"^[0-9]{12}$", info3):
            messagebox.showinfo("Error", "Please enter a valid Aadhar number")
            return
        
        # Here, you can add code to save these details to a database or another storage

        messagebox.showinfo("Success", "Customer details added successfully")
        root1.destroy()

    root1 = Tk()
    root1.title("Add Customer")
    
    Label(root1, text="Customer's Full Name").pack()
    e1 = Entry(root1)
    e1.pack()

    Label(root1, text="Contact Number").pack()
    e2 = Entry(root1)
    e2.pack()

    Label(root1, text="Identity Proof (Aadhar Number)").pack()
    e3 = Entry(root1)
    e3.pack()

    btn1 = Button(root1, text="Submit", fg='Black', bg='Light Grey', command=submit_details)
    btn2 = Button(root1, text="Exit", fg='Black', bg='Light Grey', command=root1.destroy)

    btn1.pack(pady=10)
    btn2.pack(pady=10)
    
    root1.mainloop()

def checkin():
    pass

def checkout():
    pass

root = Tk()
root.title("Hotel Management System")
root.minsize(width=400, height=400)
root.geometry("600x500")

b1 = Button(root, text="Add Customer Details", bg='Black', fg="Grey", command=add_customer)
# b2 = Button(root, text="Checkin", bg="Black", fg="Grey", command=checkin)
# b3 = Button(root, text="Checkout", bg="Black", fg="Grey", command=checkout)
b4 = Button(root, text="Exit", bg="Black", fg="Grey", command=root.destroy)

b1.pack(padx=20, pady=20)
# b2.pack(padx=20, pady=20)
# b3.pack(padx=20, pady=20)
b4.pack(padx=20, pady=20)

root.mainloop()
