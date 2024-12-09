from tkinter import *
"""Классы отдельных данных со станций. Берут данные из класса code.
При инициализации рисуют их на холсте.
Идёт прямое преобразование данных из(файл: SPLIT.py) в смотрибельный вид.
Каждый объект имеет функцию slomat(вызывает destroy()) Для обновления содержимого на экране."""
# Добавить возможность просмотра станции на карте. Первые цифры.
# Пример: 26 номер квадрата по номенклатуре, а 477 один из 999 квадратов в этом большом

'''06.05.22 Понял какой я тупой. 
Можно было не создавать отдельный виджет Canvas
на каждый раздел. А создать один виджет и на нём размещать элементы.
Таким образом можно будет расположить направление ветра поверх цифр.'''
# Исправить
# Обмозговать как прикрепить флажок к концу.


class NForm:
    def __init__(self, KH, s):
        self.N = Canvas(width=40, height=40)
        self.KH = KH
        if self.KH[s].N == 0:
            self.N.create_oval(6, 6, 34, 34, width=2)
        elif self.KH[s].N == 1:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_line(20, 6, 20, 34, width=2)
        elif self.KH[s].N == 2:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_arc(6, 6, 34, 34, start=0, extent=90, fill='black')
        elif self.KH[s].N == 3:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_arc(6, 6, 34, 34, start=0, extent=90, fill='black')
        elif self.KH[s].N == 4:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_arc(6, 6, 34, 34, start=270, extent=180, fill='black')
        elif self.KH[s].N == 5:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_arc(6, 6, 34, 34, start=270, extent=180, fill='black')
            self.N.create_line(6, 20, 34, 20, width=2)
        elif self.KH[s].N == 6:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_arc(6, 6, 34, 34, start=180, extent=270, fill='black')
        elif self.KH[s].N == 7:
            self.N.create_oval(6, 6, 34, 34, width=2, fill='black')
            self.N.create_line(20, 6, 20, 34, width=5, fill='white')
        elif self.KH[s].N == 8:
            self.N.create_oval(6, 6, 34, 34, width=2, fill='black')
        elif self.KH[s].N == 9:
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_line(11, 11, 30, 30, width=2)
            self.N.create_line(11, 30, 30, 11, width=2)
        elif self.KH[s].N == '':
            self.N.create_oval(6, 6, 34, 34, width=2)
            self.N.create_line(6, 16, 34, 16, width=2)
            self.N.create_line(6, 24, 34, 24, width=2)
        self.N.place(x=300, y=260)

    def slomat(self):
        self.N.destroy()


class CmForm:
    def __init__(self, KH, s):
        self.Cm = Canvas(width=40, height=40)
        if KH[s].Cm == 1:
            self.Cm.create_line(10, 35, 35, 10)
            self.Cm.create_line(10, 35, 35, 35)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 2:
            self.Cm.create_line(10, 35, 35, 10)
            self.Cm.create_line(20, 35, 45, 10)
            self.Cm.create_line(10, 35, 35, 35)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 3:
            self.Cm.create_arc(10, 30, 20, 40, start=180, extent=180, style=ARC)
            self.Cm.create_arc(20, 30, 30, 40, start=180, extent=180, style=ARC)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 4:
            self.Cm.create_line(10, 35, 20, 20)
            self.Cm.create_arc(10, 30, 20, 40, start=180, extent=180, style=ARC)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 5:
            self.Cm.create_line(10, 35, 20, 20)
            self.Cm.create_arc(10, 30, 20, 40, start=180, extent=180, style=ARC)
            self.Cm.create_arc(20, 30, 30, 40, start=180, extent=180, style=ARC)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 6:
            self.Cm.create_arc(10, 0, 20, 10, start=180, extent=180, style=ARC)
            self.Cm.create_arc(20, 0, 30, 10, start=180, extent=180, style=ARC)
            self.Cm.create_arc(10, 15, 30, 35, start=180, extent=-180, style=ARC)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 7:
            self.Cm.create_line(10, 35, 20, 20)
            self.Cm.create_line(10, 35, 30, 35)
            self.Cm.create_arc(10, 30, 20, 40, start=180, extent=180, style=ARC)
            self.Cm.create_arc(20, 30, 30, 40, start=180, extent=180, style=ARC)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 8:
            self.Cm.create_line(10, 30, 10, 0)
            self.Cm.create_line(30, 30, 30, 0)
            self.Cm.create_arc(10, -15, 30, 15, start=180, extent=180, style=ARC)
            self.Cm.place(x=300, y=220)
        elif KH[s].Cm == 9:
            self.Cm.create_line(10, 25, 20, 10)
            self.Cm.create_arc(10, 20, 20, 30, start=180, extent=180, style=ARC)
            self.Cm.create_arc(8, 25, 22, 35, start=180, extent=180, style=ARC)
            self.Cm.place(x=300, y=220)

    def slomat(self):
        self.Cm.destroy()


class iiiForm:
    def __init__(self, KH, s):
        self.iii = Canvas(width=200, height=40, bg='#99ff99')
        self.iii.create_text(101, 21, font='Times 15', fill="black", text=f"Cтанция №:{KH[s].iii}")
        self.iii.place(x=0, y=0)

        self.iii2 = Canvas(width=40, height=40)
        self.iii2.create_text(19, 29, font='Times 10', fill="black", text=f"ст: {s+1}")
        self.iii2.place(x=200, y=0)

    def slomat(self):
        self.iii.destroy()


class ChForm:
    def __init__(self, KH, s):
        self.Ch = Canvas(width=40, height=40)
        if KH[s].Ch == 1:
            self.Ch.create_line(0, 20, 30, 20)
            self.Ch.create_arc(10, 10, 35, 20, start=270, extent=160, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 2:
            self.Ch.create_line(0, 20, 30, 20)
            self.Ch.create_arc(10, 10, 35, 20, start=270, extent=160, style=ARC)
            self.Ch.create_arc(5, 10, 25, 20, start=270, extent=160, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 3:
            self.Ch.create_line(0, 20, 30, 20)
            self.Ch.create_arc(10, 20, 35, 30, start=300, extent=160, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 4:
            self.Ch.create_line(0, 40, 25, 20)
            self.Ch.create_arc(15, 12, 25, 22, start=310, extent=200, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 5:
            self.Ch.create_line(7, 20, 30, 20)
            self.Ch.create_arc(0, 10, 15, 20, start=270, extent=160, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 6:
            self.Ch.create_line(0, 40, 25, 20)
            self.Ch.create_arc(15, 12, 25, 22, start=310, extent=200, style=ARC)
            self.Ch.create_line(0, 37, 30, 37)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 7:
            self.Ch.create_line(7, 20, 30, 20)
            self.Ch.create_arc(23, 10, 35, 20, start=270, extent=-160, style=ARC)
            self.Ch.create_arc(0, 10, 15, 20, start=270, extent=160, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 8:
            self.Ch.create_line(7, 20, 30, 20)
            self.Ch.create_arc(23, 10, 35, 20, start=270, extent=-160, style=ARC)
            self.Ch.place(x=300, y=180)
        elif KH[s].Ch == 9:
            self.Ch.create_line(10, 35, 25, 20)
            self.Ch.create_arc(15, 12, 25, 22, start=310, extent=200, style=ARC)
            self.Ch.create_arc(10, 30, 20, 40, start=180, extent=180, style=ARC)
            self.Ch.create_arc(20, 30, 30, 40, start=180, extent=180, style=ARC)
            self.Ch.place(x=300, y=180)

    def slomat(self):
        self.Ch.destroy()


class ClForm:
    def __init__(self, KH, s):
        self.Cl = Canvas(width=40, height=40)
        if KH[s].Cl == 1:
            self.Cl.create_line(10, 20, 30, 20)
            self.Cl.create_arc(10, 13, 30, 28, start=180, extent=-180, style=ARC)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 2:
            self.Cl.create_line(10, 20, 30, 20)
            self.Cl.create_arc(10, 13, 30, 28, start=180, extent=-180, style=ARC)
            self.Cl.create_arc(15, 8, 25, 20, start=180, extent=-180, style=ARC)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 3:
            self.Cl.create_line(10, 20, 30, 20)
            self.Cl.create_arc(10, 13, 30, 28, start=180, extent=-180, style=ARC)
            self.Cl.create_arc(15, 8, 25, 20, start=180, extent=-180, style=ARC)
            self.Cl.create_line(20, 8, 20, 18)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 4:
            self.Cl.create_arc(10, 13, 30, 28, start=180, extent=-180, style=ARC)
            self.Cl.create_line(0, 20, 16, 20)
            self.Cl.create_line(24, 20, 40, 20)
            self.Cl.create_arc(16, 17, 24, 24, start=180, extent=180, style=ARC)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 5:
            self.Cl.create_line(0, 20, 16, 20)
            self.Cl.create_line(24, 20, 40, 20)
            self.Cl.create_arc(16, 17, 24, 24, start=180, extent=180, style=ARC)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 6:
            self.Cl.create_line(10, 20, 30, 20)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 7:
            self.Cl.create_line(10, 20, 14, 20)
            self.Cl.create_line(18, 20, 22, 20)
            self.Cl.create_line(26, 20, 30, 20)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 8:
            self.Cl.create_line(0, 10, 16, 10)
            self.Cl.create_line(24, 10, 40, 10)
            self.Cl.create_arc(16, 7, 24, 14, start=180, extent=180, style=ARC)
            self.Cl.create_line(10, 27, 30, 27)
            self.Cl.create_arc(10, 20, 30, 35, start=180, extent=-180, style=ARC)
            self.Cl.place(x=300, y=300)
        elif KH[s].Cl == 9:
            self.Cl.create_line(10, 20, 30, 20)
            self.Cl.create_arc(10, 13, 30, 28, start=180, extent=-180, style=ARC)
            self.Cl.create_line(13, 9, 27, 9)
            self.Cl.create_line(13, 9, 18, 14)
            self.Cl.create_line(27, 9, 22, 14)
            self.Cl.place(x=300, y=300)

    def slomat(self):
        self.Cl.destroy()


class TTTForm:
    def __init__(self, KH, s):
        self.TTT = Canvas(width=40, height=40)
        self.TTT.create_text(21, 21, font='Times 15', fill="black", text=KH[s].TTT)
        self.TTT.place(x=259, y=220)

    def slomat(self):
        self.TTT.destroy()


class pppForm:
    def __init__(self, KH, s):
        self.ppp = Canvas(width=40, height=40)
        self.ppp.create_text(21, 21, font='Times 15', fill="black", text=KH[s].ppp)
        self.ppp.place(x=341, y=260)

    def slomat(self):
        self.ppp.destroy()


class PPPPForm:
    def __init__(self, KH, s):
        self.PPPP = Canvas(width=80, height=40)
        self.PPPP.create_text(41, 21, font='Times 15', fill="black", text=KH[s].PPPP)
        self.PPPP.place(x=341, y=220)

    def slomat(self):
        self.PPPP.destroy()


class aForm:
    def __init__(self, KH, s):
        self.a = Canvas(width=40, height=40)
        if KH[s].a == '':
            self.a.place(x=381, y=260)
        elif KH[s].a == 0:
            self.a.create_line(10, 35, 30, 10)
            self.a.create_line(30, 10, 30, 20)
            self.a.place(x=381, y=260)
        elif KH[s].a == 1:
            self.a.create_line(10, 35, 30, 10)
            self.a.create_line(30, 10, 40, 10)
            self.a.place(x=381, y=260)
        elif KH[s].a == 2:
            self.a.create_line(10, 35, 30, 10)
            self.a.place(x=381, y=260)
        elif KH[s].a == 3:
            self.a.create_line(0, 26, 10, 35)
            self.a.create_line(10, 35, 30, 10)
            self.a.place(x=381, y=260)
        elif KH[s].a == 4:
            self.a.create_line(10, 21, 30, 21)
            self.a.place(x=381, y=260)
        elif KH[s].a == 5:
            self.a.create_line(0, 5, 15, 30)
            self.a.create_line(15, 30, 25, 20)
            self.a.place(x=381, y=260)
        elif KH[s].a == 6:
            self.a.create_line(0, 5, 15, 30)
            self.a.create_line(15, 30, 30, 30)
            self.a.place(x=381, y=260)
        elif KH[s].a == 7:
            self.a.create_line(0, 5, 25, 30)
            self.a.place(x=381, y=260)
        elif KH[s].a == 8:
            self.a.create_line(15, 5, 40, 30)
            self.a.create_line(15, 5, 0, 20)
            self.a.place(x=381, y=260)

    def slomat(self):
        self.a.destroy()


class wwForm:
    def __init__(self, KH, s):
        self.ww = Canvas(width=40, height=20)
        self.ww.create_text(21, 11, font='Times 10', fill="#00aa00", text=KH[s].ww)
        self.ww.place(x=259, y=260)

    def slomat(self):
        self.ww.destroy()


class VVForm:
    def __init__(self, KH, s):
        self.VV = Canvas(width=40, height=20)
        if KH[s].VV == '': self.VV.place(x=259, y=281)
        elif 0 <= KH[s].VV <= 50: self.VV.create_text(21, 11, font='Times 14', fill="black", text=KH[s].VV / 10)
        elif 56 <= KH[s].VV <= 80: self.VV.create_text(21, 11, font='Times 14', fill="black", text=KH[s].VV - 50)
        elif 81 <= KH[s].VV <= 88: self.VV.create_text(21, 11, font='Times 14', fill="black", text=30 + (KH[s].VV % 10) * 5)
        elif KH[s].VV == 89: self.VV.create_text(21, 11, font='Times 14', fill="black", text='>70')
        elif KH[s].VV == 90: self.VV.create_text(21, 11, font='Times 14', fill="black", text='<0.05')
        elif KH[s].VV == 91: self.VV.create_text(21, 11, font='Times 14', fill="black", text='0.05')
        elif KH[s].VV == 92: self.VV.create_text(21, 11, font='Times 14', fill="black", text='0.2')
        elif KH[s].VV == 93: self.VV.create_text(21, 11, font='Times 14', fill="black", text='0.5')
        elif KH[s].VV == 94: self.VV.create_text(21, 11, font='Times 14', fill="black", text='1')
        elif KH[s].VV == 95: self.VV.create_text(21, 11, font='Times 14', fill="black", text='2')
        elif KH[s].VV == 96: self.VV.create_text(21, 11, font='Times 14', fill="black", text='4')
        elif KH[s].VV == 97: self.VV.create_text(21, 11, font='Times 14', fill="black", text='10')
        elif KH[s].VV == 98: self.VV.create_text(21, 11, font='Times 14', fill="black", text='20')
        elif KH[s].VV == 99: self.VV.create_text(21, 11, font='Times 14', fill="black", text='>50')
        self.VV.place(x=259, y=281)

    def slomat(self):
        self.VV.destroy()


class TdTdTdForm:
    def __init__(self, KH, s):
        self.TdTdTd = Canvas(width=80, height=40)
        self.TdTdTd.create_text(41, 21, font='Times 15', fill="black", text=KH[s].TdTdTd)
        self.TdTdTd.place(x=220, y=300)

    def slomat(self):
        self.TdTdTd.destroy()


class ddForm:
    def __init__(self, d):
        self.dd = Canvas(width=200, height=200)
        self.dd.create_oval(98, 98, 104, 104, fill='black')
        self.dd.create_arc(5, 5, 195, 195, start=d, extent=0, fill='black')
        self.dd.place(x=0, y=200)

    def slomat(self):
        self.dd.destroy()


class ffForm:
    def __init__(self, KH, s):
        self.FF = Canvas(width=50, height=50)
        self.ff = Canvas(width=50, height=50)
        if KH[s].ff == 0:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_oval(21, 21, 31, 31)
            self.ff.place(x=75, y=140)
        elif KH[s].ff == 2 or KH[s].ff == 3:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 0)
        elif KH[s].ff == 4 or KH[s].ff == 5 or KH[s].ff == 6:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
        elif KH[s].ff == 7 or KH[s].ff == 8:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 0)
        elif KH[s].ff == 9 or KH[s].ff == 10 or KH[s].ff == 11:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 1)
        elif KH[s].ff == 12 or KH[s].ff == 13:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 1)
            self.Flag(2, 0)
        elif KH[s].ff == 14 or KH[s].ff == 15 or KH[s].ff == 16:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 1)
            self.Flag(2, 1)
        elif KH[s].ff == 17 or KH[s].ff == 18:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 1)
            self.Flag(2, 1)
            self.Flag(3, 0)
        elif KH[s].ff == 19 or KH[s].ff == 20 or KH[s].ff == 21:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 1)
            self.Flag(2, 1)
            self.Flag(3, 1)
        elif KH[s].ff == 22 or KH[s].ff == 23:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.Flag(0, 1)
            self.Flag(1, 1)
            self.Flag(2, 1)
            self.Flag(3, 1)
            self.Flag(4, 0)
        elif KH[s].ff == 24 or KH[s].ff == 25 or KH[s].ff == 26:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_line(0, 15, 40, 15)
            self.ff.create_polygon(43, 15, 45, 42, 34, 15)
            self.ff.place(x=75, y=140)
        elif KH[s].ff == 27 or KH[s].ff == 28:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 42, 34, 15)
            self.Flag(2, 0)
        elif KH[s].ff == 29 or KH[s].ff == 30 or KH[s].ff == 31:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
        elif KH[s].ff == 32 or KH[s].ff == 33:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 42, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 0)
        elif KH[s].ff == 34 or KH[s].ff == 35 or KH[s].ff == 36:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 1)
        elif KH[s].ff == 37 or KH[s].ff == 38:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 1)
            self.Flag(4, 0)
        elif KH[s].ff == 39 or KH[s].ff == 40 or KH[s].ff == 41:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 1)
            self.Flag(4, 1)
        elif KH[s].ff == 42 or KH[s].ff == 43:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 1)
            self.Flag(4, 1)
            self.Flag(5, 0)
        elif KH[s].ff == 44 or KH[s].ff == 45 or KH[s].ff == 46:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 1)
            self.Flag(4, 1)
            self.Flag(5, 1)
        elif KH[s].ff == 47 or KH[s].ff == 48:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 45, 34, 15)
            self.Flag(2, 1)
            self.Flag(3, 1)
            self.Flag(4, 1)
            self.Flag(5, 1)
            self.Flag(6, 0)
        elif KH[s].ff == 49 or KH[s].ff == 50:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_line(0, 15, 40, 15)
            self.ff.create_polygon(43, 15, 45, 42, 34, 15)
            self.ff.create_polygon(34, 15, 39, 42, 27, 15)
            self.ff.place(x=75, y=140)
        elif KH[s].ff == 51 or KH[s].ff == 52 or KH[s].ff == 53:
            self.FF.create_text(26, 46, font='Times 9', fill="black", text='Флажок:')
            self.FF.place(x=35, y=85)
            self.ff.create_polygon(43, 15, 45, 42, 34, 15)
            self.ff.create_polygon(34, 15, 39, 42, 27, 15)
            self.Flag(3, 0)

    def Flag(self, pos, chlen):
        """Упрощает размещение флага.
        позиция: pos(0, 1, 2, 3, 4)
        РАЗМЕР ИМЕЕТ ЗНАЧЕНИЕ на выбор chlen(1 #BIG, 0 #SMOLL)"""
        self.ff.create_line(0, 15, 40, 15)
        self.ff.create_line(40 - pos * 6, 15, 45 - pos * 6, 30 + chlen * 12)
        self.ff.place(x=75, y=140)

    def slomat(self):
        self.ff.destroy()
