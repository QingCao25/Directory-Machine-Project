from tkinter import *
import tkinter as tk
import os

root = tk.Tk()
root.geometry("500x500")
root.iconbitmap("C:/Users/qcao/Desktop/Directory Machine/app.ico")
root.title("Directory Builder")
bigentry = tk.IntVar()

def Get_Value(x):
    e_text = int(entry.get()) + int(entry1.get()) + int(x)
    Label(root, text=e_text,font=("Arial",18)).pack(pady=20)

label = tk.Label(root, text="Enter Information Below", font=("Arial", 18))
label.pack(padx=20, pady=20)

entry = tk.Entry(root, textvariable = bigentry, font=("Arial", 16))
entry.pack()

entry1 = tk.Entry(root, font=("Arial", 16))
entry1.pack()

def Get_Values():
    Get_Value(0)

button = tk.Button(root, text="Enter",command=Get_Values)
button.pack(padx=10,pady=10)


root.mainloop()