import model
from tkinter import * #подключение ко всей библеотеке
from tkinter import ttk  #включить определённый алг-м

root = None
frm = None


def createMenu():
    print('Меню создано!')
    printResult()

    global root
    global frm
    root = Tk()  # var random = new Random(); - создание объекта
    frm = ttk.Frame(root, padding=10) # полотно с объектами и отступы
    frm.grid() #решётка , самый простой способ расположить элементы правильно, упорядочить
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0) # текст
    ttk.Button(frm, text="Дни до нового года", command=printResult).grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=ounFunc).grid(column=1, row=5) #колонка строка кнопки #кнопка, при создании кнопки указываем какое действие ей сделать
    root.mainloop()


def printResult():
    global root
    global frm
    ttk.Label(frm, text=f'{model.newYear()} дней до нового года').grid(column=1, row=1)
    # print(f'{model.newYear()} дней до нового года')



def ounFunc():
    print('наш метод')



