#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Future Value Calculator')
root.geometry("500x350")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)


def click_button1():
    root.title("I like Python Programming, It's cool!.")

def click_button2():
    root.destroy()
    

#button1.pack()
#exitbtn.pack()

root.mainloop()
