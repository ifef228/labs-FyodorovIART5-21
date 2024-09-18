import math
import sys


class Polinom:
    def __init__(self):
        self.rootsArr = None
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0

    def getCoef(self, index, prompt):
        '''
        Читаем коэффициент из командной строки или вводим с клавиатуры
        Args:
            index (int): Номер параметра в командной строке
            prompt (str): Приглашение для ввода коэффицента
        Returns:
            float: Коэффициент квадратного уравнения
        '''
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        # Переводим строку в действительное число
        coef = float(coef_str)
        return coef

    def enterCoefs(self):
        while True:
            self.a = self.getCoef(1, "A = ")
            self.b = self.getCoef(2, "B = ")
            self.c = self.getCoef(3, "C = ")
            if self.a == 0:
                print("invalid data")
                continue
            else:
                break

    def calculate(self):

        self.enterCoefs()
        d = self.b ** 2 - 4 * self.a * self.c
        if d < 0.0:
            self.rootsArr = []
            return []
        elif d == 0.0:
            x = (-self.b) / (2 * self.a)
            self.rootsArr = self.processX(x)
        else:
            x1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(d)) / (2 * self.a)

            self.rootsArr = self.processX(x1) + self.processX(x2)
        return self.rootsArr

    @staticmethod
    def processX(x):
        if x < 0.0:
            return []
        elif x == 0.0:
            return [0.0]
        else:
            return [math.sqrt(x), -math.sqrt(x)]


def main():
    pol = Polinom()
    root = pol.calculate()

    print(root)


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
