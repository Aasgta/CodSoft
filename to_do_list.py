import tkinter as tk
from tkinter import *
import pickle

tasks =[]

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_list.insert(END,task)
        task_entry.delete(0,END)

def remove_task():
    select_item = task_list.curselection()
    if select_item:
        task_list.delete(select_item)
        for item in tasks:
            tasks.remove(item)
            
def mark_complete():
    select_item = task_list.curselection()
    if select_item:
        item = task_list.get(select_item)
        if item.startswith("✅"):
            task_list.itemconfig(select_item,fg="black")
            task_list.delete(select_item)
            task_list.insert(END,item[1:])

        else:
            task_list.itemconfig(select_item,fg="black")
            task_list.delete(select_item)
            task_list.insert(END,"✅"+item)

def save_task():
    with open("todo_list.pkl",'wb') as f:
        pickle.dump(tasks , f)
    


if __name__ == '__main__':
    window = tk.Tk()
    window.config(background = "yellow")
    window.title("GUI To Do List")
    window.geometry("650x410")

    label = tk.Label(window,text="TO DO LIST",font = ("Arial" , 20 ),justify="center")
    label.grid(row = 0,column=4)
    label.pack(side="top",fill="both")

    input_task = StringVar()
    task_entry = tk.Entry(window,font = ("Calibri" , 15 ),width = 20, textvariable=input_task,bg="light blue")
    task_entry.place(x=40,y=54)
    
    task_add = tk.Button(window,text="Add task" ,font=("Arial" , 15 , "bold"),width = 15 ,bg="dark gray",command = add_task)
    task_add.place(x=40,y=104)

    task_remove = tk.Button(window,text="Remove task" ,font=("Arial" , 15 , "bold"),width = 15,height=1 ,bg="dark gray",command = remove_task)
    task_remove.place(x=40,y=154)

    task_complete = tk.Button(window,text="Mark as completed" ,font=("Arial" , 15 , "bold"),width = 15,height=1 ,bg="dark gray",command = mark_complete)
    task_complete.place(x=40,y=204)

    task_show = tk.Button(window,text="Save tasks" ,font=("Arial" , 15 , "bold"),width = 15 ,bg="dark gray",command = save_task)
    task_show.place(x=40,y=254)

    task_list = tk.Listbox(window,font=("Helvetica" , 15 ),bg="light pink",justify="center",listvariable=tasks )
    task_list.place(x=320,y=54)

    window.mainloop()

    