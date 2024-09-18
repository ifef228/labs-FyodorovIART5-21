import math
import sys


def getCoef(index, prompt):
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


def is_valid(a):
    if a == 0:
        return False
    else:
        return True


def process_roots(x):
    if x > 0:
        return [math.sqrt(x), -math.sqrt(x)]
    elif x == 0:
        return [0]
    else:
        return []


def get_roots(a, b, d):
    if d < 0:
        return []
    elif d == 0:
        x = -b / (2 * a)
        return process_roots(x)
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return process_roots(x1) + process_roots(x2)


def calculate_roots():
    a = 0.0
    b = 0.0
    c = 0.0
    while not is_valid(a):
        a = getCoef(1, "A = ")
        b = getCoef(1, "B = ")
        c = getCoef(1, "C = ")
    d = (b ** 2) - 4 * a * c
    return get_roots(a, b, d)


def main():
    print(calculate_roots())


if __name__ == '__main__':
    main()
