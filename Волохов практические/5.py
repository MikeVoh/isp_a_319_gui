from tkinter import *

persons = {
    'Александр': '+79635421236',
    'Константин': '+79635452398',
    'Михаил': '+79635445289',
    'Василий': '+79635412547',
    'Макс': '+79635465123'
}

def get_info():
    label.config(text=persons[var.get()])

root = Tk()
root.title('Информация о сотруднике')
root.resizable(height=False, width=False)

f_left = Frame(root)
f_left.pack(side=LEFT)

label = Label(root, justify='center', width=40, text='Выберите сотрудника', font=18)
label.pack(side=LEFT, expand=True)

var = StringVar()

for name in persons.keys():
    Radiobutton(f_left, width=20, font = 20, text=name, indicatoron=0, variable=var,
        value=name, command=get_info).pack(side=TOP)

root.mainloop()