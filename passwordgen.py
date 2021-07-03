from tkinter import *
from tkinter.ttk import Combobox
import random

root = Tk()
root.title("Password Generator")
root.geometry("320x300")
root.configure(bg="gray64")
root.columnconfigure(0,weight=1)
root.resizable(False,False)

def gen():
    global string
    string.set("")
    passw=" "
    length=int(lenght_entry.get())
    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mixs="0123456789"+lowercase+uppercase+"@#$&*"

    if strenght_combobox.get()=="Low Strength":
        for i in range(0,length):
            passw=passw+random.choice(lowercase)
        string.set(passw)

    elif strenght_combobox.get()=="Medium Strength":
        for i in range(0,length):
            passw=passw+random.choice(uppercase)
        string.set(passw)

    elif strenght_combobox.get()=="High Strength":
        for i in range(0,length):
            passw=passw+random.choice(mixs)
        string.set(passw)


string = StringVar("")
name_label = Label(root,text="Password Generator",font=("Arial",22,"bold"),bg="gray64").grid()
lenght_label = Label(root,text="Length:",font=("Arial",14,"bold"),bg="gray64").grid()
lenght_entry = Entry(root,font=("Arial",14),width=15,relief="ridge",borderwidth=4)
lenght_entry.grid()
strenght_label = Label(root,text="Strength:",font=("Arial",14,'bold'),bg="gray64").grid()

strenght_combobox = Combobox(root,font=("Arial",14),width=15,state="readonly")
strenght_combobox["values"]=("Low Strength","Medium Strength","High Strength")
strenght_combobox.current(1)
strenght_combobox.grid()

generate_button = Button(root,text="Generate",bg="gray74",width=10,relief="ridge",borderwidth=4,command=gen).grid()
password_label = Label(root,text="Password:",font=("Arial",14,"bold"),bg="gray64").grid()
password_entry = Entry(root,font=("Arial",14),textvariable=string,relief="ridge",borderwidth=4).grid()
made_by_label = Label(root,text="Made By Harun",font=("Arial",20,"bold"),bg="gray64").grid()

root.mainloop()
