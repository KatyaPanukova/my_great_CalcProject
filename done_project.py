# Задача:
# написать программу- калькулятор(внешний интерфейс:калькулятор с различными кнопками).
# Обязательны функции рассчета :суммы,разности,произведения,деления,
# возведения в степень.А также взятие процента, отдельные кнопки для вычисления
# корней кубического и квадратного уравнений.Оригинальный дизайн.
# (Добавление голосового ассистента).

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('E_CALCULATOR')

all_button = [
    'AC', '//', '%', '÷',
    '7', '8', '9', 'х',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=', 'SQRT']

light = 1
wight = 0

for i in all_button:
    firs = ''
    button_1 = ttk.Button(root, text=i).grid(row=light, column=wight)
    wight += 1
    if wight > 3:
        wight = 0
        light += 1

root.mainloop()
