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
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} за 1 доллар')
            else:
                mb.showerror('Ошибка!', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}.')
    else:
        mb.showwarning('Внимание!', 'Введите код валюты!')


root = Tk()
root.title('Кусры обмена валют')
root.geometry('500x500')

Label(root, text='Выберите код валюты').pack(padx=10, pady=10)

cur = ['RUB', 'EUR', 'GBP', 'CNY', 'KXT', 'UZS', 'CHF', 'AED', 'CAD']
combobox = ttk.Combobox(root, values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry(root)
# entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

root.mainloop()
