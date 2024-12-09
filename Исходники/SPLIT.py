def split(kod):
    """Делит строку на двумерный массив
    сперва по =(станции) затем по пробелам(Данные со станции).
    Возвращает отформатированный массив."""
    mass = kod.split('=')
    a = []
    for b in range(len(mass)): a.append(mass[b].split())
    return a


class code:
    """Принимает на вход массив(Я использую одну станцию/строку КН-01)
    на выходе получаем объект с дешифрованными переменными."""

    def __init__(self, kod):
        self.kod = kod
        self.iii = ''
        self.VV = ''
        self.N = ''
        self.dd = ''
        self.ff = ''
        self.TTT = ''
        self.TdTdTd = ''
        self.PoPoPo = ''
        self.PPPP = ''
        self.ppp = ''
        self.a = ''
        self.ww = ''
        self.Wi = ''
        self.Wt = ''
        self.Cl = ''
        self.Cm = ''
        self.Ch = ''
        """try и except это проверка на  / - отсутствие данных на станции """
        try:
            self.iii = int(self.kod[0][9]) + int(self.kod[0][8]) * 10 + int(self.kod[0][7]) * 100
        except:
            self.iii = ''

        try:
            self.VV = int(self.kod[1][4]) + int(self.kod[1][3]) * 10
        except:
            self.VV = ''

        try:
            self.N = int(self.kod[2][0])
        except:
            self.N = ''

        try:
            self.dd = int(self.kod[2][2]) + int(self.kod[2][1]) * 10
        except:
            self.dd = ''

        try:
            self.ff = int(self.kod[2][4]) + int(self.kod[2][3]) * 10
        except:
            self.ff = ''

        try:
            if self.kod[3][1] == '0':
                self.TTT = int(self.kod[3][4]) + int(self.kod[3][3]) * 10 + int(
                    self.kod[3][2]) * 100
            else:
                self.TTT = int(self.kod[3][4]) + int(self.kod[3][3]) * 10 + int(self.kod[3][2]) * -100
        except:
            self.TTT = ''

        try:
            if self.kod[3][1] == '0':
                self.TdTdTd = int(self.kod[4][4]) + int(self.kod[4][3]) * 10 + int(
                    self.kod[4][2]) * 100
            else:
                self.TdTdTd = int(self.kod[4][4]) + int(self.kod[4][3]) * 10 + int(self.kod[4][2]) * -100
        except:
            self.TdTdTd = ''

        try:
            self.PoPoPo = int(self.kod[5]) % 10000
        except:
            self.PoPoPo = ''

        try:
            self.PPPP = (int(self.kod[6]) % 10000) / 10
            if self.PPPP < 900:
                self.PPPP += 1000
        except:
            self.PPPP = ''

        try:
            self.ppp = int(self.kod[7][4]) + int(self.kod[7][3]) * 10 + int(self.kod[7][2]) * 100
        except:
            self.ppp = ''

        try:
            self.a = int(self.kod[7][1])
        except:
            self.a = ''

        for i in range(6, len(self.kod)):
            if self.kod[i][0] == '7':

                try:
                    self.ww = int(self.kod[i][2]) + int(self.kod[i][1]) * 10
                except:
                    self.ww = ''

                try:
                    self.Wi = int(self.kod[i][3])
                except:
                    self.Wi = ''

                try:
                    self.Wt = int(self.kod[i][4])
                except:
                    self.Wt = ''

            if self.kod[i][0] == '8':
                try:
                    self.Cl = int(self.kod[i][2])
                except:
                    self.Cl = ''

                try:
                    self.Cm = int(self.kod[i][3])
                except:
                    self.Cm = ''

                try:
                    self.Ch = int(self.kod[i][4])
                except:
                    self.Ch = ''

    def Printer(self):
        """Для проверки. Выводит дешифрованные данные"""
        print(
            f"\niii: {self.iii}\nVV: {self.VV}\nN: {self.N}\ndd: {self.dd}\nff: {self.ff}\nTTT: {self.TTT}\nTdTdTd: {self.TdTdTd}\nPoPoPo: {self.PoPoPo}\nPPPP: {self.PPPP}\nppp: {self.ppp}a: {self.a}\nww: {self.ww}\nWi: {self.Wi}\nWt: {self.Wt}\nCl: {self.Cl}\nCm: {self.Cm}\nCh: {self.Ch}")
