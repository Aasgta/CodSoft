import tkinter as tk
from tkinter import *

string = ""

def press(num):
    global string
    string +=str(num)        #concatenation of string
    input_text.set(string)


def clear():
    global string
    string = ""
    input_text.set("")

def equalTo():
    try:
        global string
        result = str(eval(string))     #str convert the integer to string
        input_text.set(result) 
        string=""
    except:
        input_text.set("error")
        string=""


if __name__ =='__main__':
    
    window = tk.Tk()
    window.title("Calculator")
    window.configure(background="silver")
    window.geometry("500x400")
   
    input_text = StringVar()

    first_entry = tk.Entry(window ,font = ("Arial" , 30 ),width = 15,textvariable=input_text, justify="right",bd=0,bg="light green")
    first_entry.grid(row =0,columnspan=4, ipadx=70)
    

    #  row1
    #clear operation
    buttonc =tk.Button(window,text="C" ,font=("Arial" , 25 , "bold"),width =10, height = 1,bg = "red",command = clear)             
    buttonc.grid(row = 1, column = 0, columnspan = 3, padx = 1, pady = 1) 

    #divide
    buttond =tk.Button(window,text="/" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="dark gray",command = lambda:press("/"))           
    buttond.grid(row = 1, column = 3, padx = 1, pady = 1)

    # row2
    #num keys
    button7 =tk.Button(window,text="7" ,font=("Arial" , 25 , "bold"), width = 3, height = 1,bg="light gray", command =lambda: press(7))
    button7.grid(row = 2, column = 0, padx = 1, pady = 1)
    
    button8 =tk.Button(window,text="8" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg = "light gray",command =lambda: press(8))
    button8.grid(row = 2, column = 1, padx = 1, pady = 1)
    
    button9 =tk.Button(window,text="9" ,font=("Arial" , 25 , "bold"),width =3, height = 1,bg="light gray",command =lambda: press(9))
    button9.grid(row = 2, column = 2, padx = 1, pady = 1)

    #multiplication
    buttonm =tk.Button(window,text="*" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="dark gray",command = lambda:press("*"))
    buttonm.grid(row = 2, column = 3, padx = 1, pady = 1)

    #row3
    #num keys
    button4 =tk.Button(window,text="4" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="light gray",command =lambda: press(4))
    button4.grid(row = 3, column = 0, padx = 1, pady = 1)
    
    button5 =tk.Button(window,text="5" ,font=("Arial" , 25 , "bold"),width =3, height = 1,bg="light gray",command =lambda: press(5))
    button5.grid(row = 3, column = 1, padx = 1, pady = 1)
    
    button6 =tk.Button(window,text="6" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="light gray",command =lambda: press(6))
    button6.grid(row = 3, column = 2, padx = 1, pady = 1)
 
     #subtraction
    buttons =tk.Button(window,text="-" ,font=("Arial" , 25 , "bold"),width =3, height = 1,bg="dark gray",command = lambda:press("-"))
    buttons.grid(row = 3, column = 3, padx = 1, pady = 1)

    #row4
    # num keys
    button1 =tk.Button(window,text="1" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="light gray",command =lambda: press(1))
    button1.grid(row = 4, column = 0, padx = 1, pady = 1)
    
    button2 =tk.Button(window,text="2" ,font=("Arial" , 25 , "bold"),width =3, height = 1,bg="light gray",command =lambda: press(2))
    button2.grid(row = 4, column = 1, padx = 1, pady = 1)
    
    button3 =tk.Button(window,text="3" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="light gray",command =lambda: press(3))
    button3.grid(row = 4, column = 2, padx = 1, pady = 1)

    #addition
    buttona =tk.Button(window,text="+" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="dark gray",command = lambda:press("+"))
    buttona.grid(row = 4, column = 3, padx = 1, pady = 1)

    #row5
    #num key
    button0 =tk.Button(window,text="0" ,font=("Arial" , 25 , "bold"),width = 5, height = 1,bg="light gray",command=lambda:press("0"))
    button0.grid(row = 5, column = 0, columnspan = 2, padx = 1, pady = 1)

    #decimal point
    buttonp =tk.Button(window,text="." ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="light gray",command=lambda:press("."))
    buttonp.grid(row = 5, column = 2, padx = 1, pady = 1)
    
    #equal to
    buttoneq =tk.Button(window,text="=" ,font=("Arial" , 25 , "bold"),width = 3, height = 1,bg="dark gray",command = equalTo)
    buttoneq.grid(row = 5, column = 3, padx = 1, pady = 1)

    window.mainloop()
    
    
