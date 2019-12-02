import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('E_CALCULATOR')

all_button = [
    'AC', '//', '%', '÷',
    '7', '8', '9', 'х',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=']

light = 1
wight = 0

for i in all_button:
    firs = ''
    buttn_1 = ttk.Button(root, text=i).grid(row=light, column=wight)
    wight += 1
    if wight > 4:
        wight = 0
        light += 1

root.mainloop()
