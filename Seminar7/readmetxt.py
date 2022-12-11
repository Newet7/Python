
from tkinter import * #подключение ко всей библеотеке
from tkinter import ttk  #включить определённый алг-м

def ounFunc():
    print('наш метод')



root = Tk()  # var random = new Random(); - создание объекта
frm = ttk.Frame(root, padding=10) # полотно с объектами и отступы
frm.grid() #решётка , самый простой способ расположить элементы правильно, упорядочить
ttk.Label(frm, text="Hello World!").grid(column=0, row=0) # текст
ttk.Button(frm, text="Quit", command=ounFunc).grid(column=1, row=0) #колонка строка кнопки #кнопка, при создании кнопки указываем какое действие ей сделать
root.mainloop()
