from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import nametofont
from idlelib.tooltip import Hovertip
from RAScal_5_INPUT import input_value
from RAScal_5_CONVERT import convert_value


def enable_choice():  # переключение доступности кнопок для выбора типа кода
    if convert_type.get() == 2 or convert_type.get() == 3:  # если выбран перевод из кода
        code_type.set(0)
        strcode.configure(state='normal')
        revcode.configure(state='normal')
        addcode.configure(state='normal')
    else:
        code_type.set(0)
        strcode.configure(state='disabled')
        revcode.configure(state='disabled')
        addcode.configure(state='disabled')


def show_error(error_type):  # вывод ошибки
    # принимает: тип ошибки (str)
    # выводит сообщение об ошибке в соответствии с кодом
    if error_type == '01':
        messagebox.showerror(parent=window, title='Ошибка', message='Вы не ввели тип перевода.')
    elif error_type == '02':
        messagebox.showerror(parent=window, title='Ошибка', message='Вы не ввели тип кода.')
    elif error_type == '03':
        messagebox.showerror(parent=window, title='Ошибка', message='Вы не ввели значение.')
    elif error_type == '10':
        messagebox.showerror(parent=window, title='Ошибка', message='Число должно содержать только '
                                                                    'десятичные цифры и '
                                                                    'одиночный знак + или - перед числом.')
    elif error_type == '11':
        messagebox.showerror(parent=window, title='Ошибка', message='Ошибка. Число не должно начинаться с нуля.')
    elif error_type == '12':
        messagebox.showerror(parent=window, title='Ошибка', message='Ошибка. Число должно быть целым.')
    elif error_type == '13':
        messagebox.showerror(parent=window, title='Ошибка', message='Ошибка. Число должно быть в диапазоне от '
                                                                    '-(2^63 - 1) до 2^63 - 1.')
    elif error_type == '20':
        messagebox.showerror(parent=window, title='Ошибка', message='Введены недопустимые символы.')
    elif error_type == '21':
        messagebox.showerror(parent=window, title='Ошибка', message='Превышена максимальная длина.')
        correct_input = False
    elif error_type == '22':
        messagebox.showerror(parent=window, title='Ошибка', message='Код не должен '
                                                                    'состоять меньше чем из двух символов ')
    elif error_type == '23':
        messagebox.showerror(parent=window, title='Ошибка', message='Обратный код не должен '
                                                                    'состоять только из единиц.')
    elif error_type == '24':
        messagebox.showerror(parent=window, title='Ошибка', message='Дополнительный код не должен '
                                                                    'состоять только из нулей.')
    elif error_type == '30':
        messagebox.showerror(parent=window, title='Ошибка', message='Введены недопустимые символы. '
                                                                    'Убедитесь, что буквы написаны в нижнем регистре.\n'
                                                                    'Алфавит шестнадцатеричной '
                                                                    'системы: 0123456789abcdef')
    elif error_type == '31':
        messagebox.showerror(parent=window, title='Ошибка', message='Превышена максимальная длина.')
    elif error_type == '32':
        messagebox.showerror(parent=window, title='Ошибка', message='Обратный код не должен '
                                                                    'состоять только из единиц.')
    elif error_type == '33':
        messagebox.showerror(parent=window, title='Ошибка', message='Дополнительный код не должен '
                                                                    'состоять только из нулей.')


def show_result(result):  # вывод результатов в таблице
    # принимает: список кортежей со значениями для вывода (list)
    # возвращает:
    global table
    table.delete(*table.get_children())
    table.destroy()
    table = ttk.Treeview()
    if len(result) == 3:  # если перевели в коды
        crutch = Label(window, text=result[0][1])
        crutch.grid(row=6, column=0, ipadx=20)
        window.update_idletasks()
        cell_size = crutch.winfo_width()
        crutch.destroy()
        results.grid(row=5, column=0)
        columns = ('1', '2', '3')
        table.config(columns=columns, show='headings', height=3)
        table.heading('1', text='', anchor='center')
        table.column('1', anchor='center')
        table.heading('2', text='Двоичный', anchor='center')
        table.column('2', anchor='center', width=cell_size)
        table.heading('3', text='Шестнадцатеричный', anchor='center')
        table.column('3', anchor='center')
    elif len(result) == 1:  # если перевели в число
        results.grid(row=5, column=0)
        columns = ('0', '1')
        table.config(columns=columns, show='headings', height=1)
        table.heading('0', text='Код', anchor='center')
        table.column('0', anchor='center', )
        table.heading('1', text='Число', anchor='center')
        table.column('1', anchor='center')
    for data in result:
        table.insert('', END, values=data)
    table.grid(row=5, column=1, columnspan=3, pady=[0, 20], padx=[0, 20])


def input_convert_show():  # проверка ввода, перевод и вывод результатов или ошибки
    result_of_input = input_value(convert_type.get(), code_type.get(), valinput.get())
    if result_of_input[0]:  # если ввод корректен
        results = convert_value(convert_type.get(), code_type.get(), valinput.get())
        show_result(results)
    else:
        show_error(result_of_input[1])


def show_refer():
    refer = Toplevel()
    refer.title("Справка")
    refer.iconphoto(False, PhotoImage(file="ReferImage.png"))
    ref_text = Label(refer, text="Пример перевода числа 10 в коды.\n"
                                 "I. ПЕРЕВОД В ПРЯМОЙ КОД\n"
                                 "1. Чтобы перевести число в прямой код сначала нужно перевести модуль числа в двоичную систему, а затем добавить слева знаковый бит: 1 если число меньше 0 и 0 если число больше 0.\n"
                                 "2. Так как 10>0, то знаковый бит равен 0.\n"
                                 "3. Двоичное представление числа 10 равно 0001010.\n"
                                 "4. Добавляя слева знаковый бит, получаем прямой код числа 10 равным 00001010; Переводя код в 16-ричную систему, включая знаковый бит, получаем 0a.\n"
                                 "II. ПЕРЕВОД В ОБРАТНЫЙ КОД\n"
                                 "1. Обратный код для положительного числа совпадает с прямым, а для отрицательного числа все цифры заменяются на противоположные (1 на 0, 0 на 1), в знаковый бит записывается 1.\n"
                                 "2. Так как 10>0, то обратный код соответствует прямому\n"
                                 "3. Добавляя слева знаковый бит, получаем обратный код числа 10 равным 00001010; Переводя код в 16-ричную систему, включая знаковый бит, получаем 0a.\n"
                                 "III. ПЕРЕВОД В ДОПОЛНИТЕЛЬНЫЙ КОД\n"
                                 "1. Дополнительный код для положительного числа совпадает с прямым, а для отрицательного числа к младшему разряду обратного кода добавляется 1.\n"
                                 "2. Так как 10>0, то дополнительный код соответствует прямому и равен 00001010; Переводя код в 16-ричную систему, включая знаковый бит, получаем 0a.)\n")
    ref_text.pack()
    # x = window.winfo_x() + ((window.winfo_width() / 2) - 175)
    # y = window.winfo_y() + ((window.winfo_height() / 2) - 175)
    # refer.geometry('%dx%d+%d+%d' % (350, 350, x, y))
    refer.grab_set()


window = Tk()  # основное окно
window.resizable(False, False)  # блокировка возможности изменения размеров окна

# иконка основного окна
window.title('RAScal 5')
icon = PhotoImage(file="RAScal-logo.png")
window.iconphoto(True, icon)

# установка одинакового размера шрифта для всех виджетов
nametofont("TkHeadingFont").configure(size=10)
nametofont("TkDefaultFont").configure(size=10)


refer_image = PhotoImage(file="ReferImage.png").subsample(20)
refer_button = Button(window, image=refer_image, borderwidth=0, command=show_refer)
refer_tip = Hovertip(refer_button, "Справка")
refer_button.grid(row=0, column=4, sticky=NE)


tips = ['Вид перевода:', 'Тип кода:', 'Значение:', 'Результаты:']  # надписи, поясняющие кнопки выбора, поле ввода и
# таблицу с результатами

# размещение поясняющих надписей у левой границы окна
Label(window, text=tips[0]).grid(row=1, column=0)  # пояснение кнопок типа перевода
Label(window, text=tips[1]).grid(row=2, column=0, pady=[0, 20])  # пояснение кнопок типа кода
Label(window, text=tips[2]).grid(row=3, column=0)  # пояснение поля ввода
results = Label(window, text=tips[3])  # пояснение таблицы с результатами

convert_type = IntVar()  # переменная, хранящая тип перевода
code_type = IntVar()  # переменная, хранящая тип кода
code_type.set(0)
code_type.set(0)

todec = Radiobutton(window, text='Из десятичного числа\nв коды',
                    variable=convert_type, value=1, command=enable_choice, indicatoron=0)  # кнопка перевода из числа
bindec = Radiobutton(window, text='Из двоичного кода\nв число',
                     variable=convert_type, value=2, command=enable_choice, indicatoron=0)  # кнопка перевода в 2ич код
hexdec = Radiobutton(window, text='Из шестнадцатеричного кода\nв число',
                     variable=convert_type, value=3, command=enable_choice, indicatoron=0)  # кнопка перевода в 16ич код

# размещение кнопок типа перевода в первом ряду слева направо
todec.grid(row=1, column=1, pady=20, padx=20)
bindec.grid(row=1, column=2, padx=20)
hexdec.grid(row=1, column=3, padx=20)

strcode = Radiobutton(window, text='Прямой код', indicatoron=0,
                      variable=code_type, value=1, state='disabled')  # кнопка прямого кода
revcode = Radiobutton(window, text='Обратный код', indicatoron=0,
                      variable=code_type, value=2, state='disabled')  # кнопка обратного кода
addcode = Radiobutton(window, text='Дополнительный код', indicatoron=0,
                      variable=code_type, value=3, state='disabled')  # кнопка дополнительного кода

# размещение кнопок типа кода во втором ряду слева направо
strcode.grid(row=2, column=1, pady=[0, 20])
revcode.grid(row=2, column=2, pady=[0, 20])
addcode.grid(row=2, column=3, pady=[0, 20])
window.update_idletasks()

# выравнивание кнопок типа кода по центру относительно кнопок типа перевода
strcode.grid_configure(ipadx=(todec.winfo_width() - strcode.winfo_width()) / 2)
revcode.grid_configure(ipadx=(bindec.winfo_width() - revcode.winfo_width()) / 2)
addcode.grid_configure(ipadx=(hexdec.winfo_width() - addcode.winfo_width()) / 2)

valinput = Entry(window, borderwidth=1, relief='solid')  # поле ввода значения
valinput.grid(row=3, column=1, sticky=NSEW, columnspan=3, padx=20)  # размещение поля ввода длиной в три колонки
# в третьем ряду

global table
table = ttk.Treeview()  # таблица результатов

submit = Button(window, text='Перевести', font="TkDefaultFont 11", command=input_convert_show)  # кнопка запуска
# перевода
submit.grid(row=4, column=2, pady=20)  # размещение кнопки перевода под полем ввода во второй колонке

window.eval('tk::PlaceWindow . center')  # размещение окна по центру экрана
window.mainloop()
