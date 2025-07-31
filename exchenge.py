import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    pass


root = Tk()
root.title('Кусры обмена валют')
root.geometry('500x500')

Label(root, text='ВВедите код валюты').pack(padx=10, pady=10)

entry = Entry(root)
entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

root.mainloop()
