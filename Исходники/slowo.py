from dannie import *


class Word:
    """Объединяет разделённые ранее на отдельные классы (файл dannie.py) в один класс для простоты вывода"""
    def __init__(self, KH, s):
        """Без понятия зачем, но инициализируем переменные, а то PyCharm жалуется"""
        self.dd = None
        self.Cm = None
        self.a = None
        self.ww = None
        self.Cl = None
        self.Ch = None
        self.TdTdTd = None
        self.TTT = None
        self.N = None
        self.VV = None
        self.iii = None
        self.PPPP = None
        self.ppp = None
        self.ff = None
        self.KH = KH
        self.s = s

    def STROIT(self):
        """Создаю объекты классов (см. файл dannie.py) при инициализации сразу выводятся на холст"""
        self.iii = iiiForm(self.KH, self.s)
        self.VV = VVForm(self.KH, self.s)
        self.N = NForm(self.KH, self.s)
        self.TTT = TTTForm(self.KH, self.s)
        self.TdTdTd = TdTdTdForm(self.KH, self.s)
        self.PPPP = PPPPForm(self.KH, self.s)
        self.ppp = pppForm(self.KH, self.s)
        self.a = aForm(self.KH, self.s)
        self.ww = wwForm(self.KH, self.s)
        self.Cl = ClForm(self.KH, self.s)
        self.Cm = CmForm(self.KH, self.s)
        self.Ch = ChForm(self.KH, self.s)
        self.ff = ffForm(self.KH, self.s)
        try:
            self.dd = ddForm((self.KH[self.s].dd*(-10))+90)
        except:
            self.dd = Canvas(width=200, height=200)
            self.dd.create_text(101, 101, font='Times 14', fill="black", text='Данные о направлении \n   ветра отсутствуют')
            self.dd.place(x=0, y=200)

    def SLOMAT(self):
        """Устрой дестрой, порядок — это отстой.
        Круши, ломай, тряси башкою пустой.
         Допей, разбей и новую открывай Давай-давай!"""
        self.iii.slomat()
        self.VV.slomat()
        self.N.slomat()
        self.TTT.slomat()
        self.TdTdTd.slomat()
        self.PPPP.slomat()
        self.ppp.slomat()
        self.a.slomat()
        self.ww.slomat()
        self.Cl.slomat()
        self.Cm.slomat()
        self.Ch.slomat()
        self.ff.slomat()
        '''Костыль. Работает - не трогай.'''
        try: self.dd.slomat()
        except: self.dd.destroy()
        '''Костыль. Работает - не трогай'''
