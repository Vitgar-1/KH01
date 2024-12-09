from slowo import *
from SPLIT import *

"""Debug information:
Программа тестировалась на версиях:
Python 3.8
tkinter 8.6
pyinstaller 5.0.1
Windows 7, 11
"""

# Узнать как обойти Windows Defender.

Window = Tk()
Window.title('Vitgar КН-01 Version 1.2')
Window.geometry('700x600+500+100')

count = 0
kod3 = []
wrd = []


def text():
    global kod3, wrd, count
    popa = KodBullet.get()
    kod3 = split(popa)
    # Сам код который дешифруем.

    KH = [code(kod3[i]) for i in range(len(kod3))]
    # Создаёт массив из объектов класса code. Каждый объект данные с отдельной станции.

    wrd = [Word(KH, i) for i in range(len(kod3))]
    if popa != '':
        wrd[count].STROIT()

        # Основные кнопки и элементы интерфейса. Ничего что может сломаться.

        btn = Button(Window, text='Разработал: Гашников Виктор (Далее)', activeforeground='#00ff00', command=lambda: UP())
        btn.place(x=450, y=550)
        btn2 = Button(Window, text='(Назад)', activeforeground='#00ff00', command=lambda: Down())
        btn2.place(x=380, y=550)


def UP():
    global count
    count += 1
    if count < len(kod3):
        wrd[count - 1].SLOMAT()
        wrd[count].STROIT()
    else:
        wrd[count - 1].SLOMAT()
        count = 0
        wrd[count].STROIT()


# Добавить возможность переключения(поиска) между станциями


def Down():
    global count
    count -= 1
    if count >= 0:
        wrd[count + 1].SLOMAT()
        wrd[count].STROIT()
    else:
        wrd[0].SLOMAT()
        count = len(kod3) - 1
        wrd[count].STROIT()


# Ввод данных.
KodBullet = StringVar()
message_entry = Entry(textvariable=KodBullet)
message_entry.place(x=380, y=10)

btn3 = Button(text="Let's GO!", activeforeground='#00ff00', command=lambda: text())
btn3.place(x=380, y=60)


def About():
    """Гордеев турбо топ!"""
    a = Toplevel()
    a.geometry('465x100')
    a['bg'] = '#ddffdd'
    a.overrideredirect(True)
    Label(a,
          text="Поддержать проект рублём можно по номеру +79932051512\n Получить исходный код для "
               "изучения\усовершенствования. Писать в Вк: @1vitgar\nПо ошибкам писать В ВК: @1vitgar") \
        .pack(expand=1)
    a.after(20000, lambda: a.destroy())


About()

Window.mainloop()
