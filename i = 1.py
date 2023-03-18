from tkinter import *
from tkinter import messagebox

def button_1():
    messagebox.showinfo ('Результат', int(a.get()) * int(b.get()))
def button_2():
    messagebox.showinfo ('Результат', int(a.get()) / int(b.get()))
def button_3():
    messagebox.showinfo ('Результат', int(a.get()) + int(b.get()))
def button_4():
    messagebox.showinfo ('Результат', int(a.get()) - int(b.get()))

root=Tk()
root.title('Калькулятор')
root.geometry('500x300')

a=Entry(root, width=10,  bg='grey', fg='cyan', font='consolas')
a.pack()
b=Entry(root, width=10,  bg='grey', fg='cyan', font='consolas')
b.pack()

Button(root, text = "*", width = 5, height = 2, command = button_1, bg="grey").pack()
Button(root, text = "/", width = 5, height = 2, command = button_2, bg="grey").pack()
Button(root, text = "+", width = 5, height = 2, command = button_3, bg="grey").pack()
Button(root, text = "-", width = 5, height = 2, command = button_4, bg="grey").pack()

root.mainloop()

