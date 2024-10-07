import tkinter as tk
from tkinter import *

contacts =[]
    
def add_contact():
    global name
    global phoneNum
    global emailAdd
    contacts.append([entry1.get(),entry2.get(),entry3.get()])
    contacts.sort()
    listBox.delete(0,END)
    for name,phoneNum,emailAdd in contacts:
        listBox.insert(END,name)
    clearEntry()

def remove_contact():
    global name
    global phoneNum
    global emailAdd
    select_contact = int(listBox.curselection()[0])
    del contacts[select_contact]
    contacts.sort()
    listBox.delete(0,END)
    for name,phoneNum,emailAdd in contacts:
        listBox.insert(END,name)
 
def view_contact():
    select_contact = int(listBox.curselection()[0])  
    name =contacts[select_contact]
    phoneNum = contacts[select_contact]
    emailAdd = contacts[select_contact]
    
    if contacts:
        view_contact = tk.Toplevel(root)
        view_contact.title("Contact Info")

        for info in contacts:
            tk.Label(view_contact,text = f"Details :{info}").place(x=1, y=3)
        
def clearEntry():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("1000x500")

    name = StringVar()
    phoneNum = StringVar()
    emailAdd = StringVar()

    label = tk.Label(root , text="Contact Book" , bg="Light Pink" , font=("Arial" , 20 , "bold"))
    label.pack(fill="both",side="top")

    label1 = tk.Label(root , text="Name :" , bg="Light blue" , font=("Arial" , 15 , "bold"))
    label1.place(x= 50 ,y=50)
    entry1 = tk.Entry(root , font=("Arial" , 15 ),textvariable=name)
    entry1.place(x=200,y=50)

    label2 = tk.Label(root , text="Phone No. :" , bg="Light blue" , font=("Arial" , 15 , "bold"))
    label2.place(x= 50 ,y=100)
    entry2 = tk.Entry(root , font=("Arial" , 15 ),textvariable=phoneNum)
    entry2.place(x=200,y=100)

    label3 = tk.Label(root , text="Email Add :" , bg="Light blue" , font=("Arial" , 15 , "bold"))
    label3.place(x= 50,y=150)
    entry3 = tk.Entry(root , font=("Arial" , 15 ),textvariable=emailAdd)
    entry3.place(x=200,y=150)

    listBox = tk.Listbox(root , width = 60,height=10,bg="light green",font=("Arial" , 15 , "bold"))
    listBox.place(x=300,y=200,anchor="nw")

    button = tk.Button(root , text = "Add contact" , fg="red" , bg="black" ,font = ("Arial" , 15 , "bold") ,command = add_contact)
    button.place(x=70,y=200)
    
    button = tk.Button(root , text = "Remove contact" , fg="red" , bg="black" ,font = ("Arial" , 15 , "bold") ,command = remove_contact)
    button.place(x=70,y=250)

    button = tk.Button(root , text = "View contact" , fg="red" , bg="black" ,font = ("Arial" , 15 , "bold") ,command = view_contact)
    button.place(x=70,y=300)

    root.mainloop() 




