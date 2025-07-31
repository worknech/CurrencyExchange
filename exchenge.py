import requests
import json
from tkinter import *
from tkinter import messagebox as mb, ttk


def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data['rates']:
                exchange_rate = data['rates'][code]
                c_name = cur[code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {c_name} за 1 доллар')
            else:
                mb.showerror('Ошибка!', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)


cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'CNY': 'Японская йена',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЕ',
    'CAD': 'Канадский доллар'
}

root = Tk()
root.title('Кусры обмена валют')
root.geometry('500x500')

Label(root, text='Выберите код валюты').pack(padx=10, pady=10)

combobox = ttk.Combobox(root, values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_c_label)

c_label = ttk.Label(root)
c_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

root.mainloop()
