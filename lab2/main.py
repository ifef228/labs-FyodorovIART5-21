from time import sleep

from lab2.cm_timer import CmTimer1, cm_timer2
from lab2.field import field
from lab2.genRandom import gen_random
from lab2.unique import Unique
from lab2.decorator import *


def main():
    # задание 1
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(field(goods, "title"))
    print(field(goods, "title", "price"))

    # задание 2
    print(gen_random(5, 1, 3))

    # задание 3
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique = Unique(data)
    print([unique.__next__() for i in range(2)])
    data = gen_random(10, 1, 3)
    unique = Unique(data)
    print([unique.__next__() for i in range(3)])
    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    unique = Unique(data)
    print([unique.__next__() for i in range(4)])
    unique = Unique(data, ignore_case=True)
    print([unique.__next__() for i in range(2)])

    # задание 4
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

    result = sorted(data, key=abs)
    print(result)

    result_lambda = sorted(data, key=lambda value: abs(value))
    print(result_lambda)

    # задание 5
    test_1()
    test_2()
    test_3()
    test_4()

    #6
    with CmTimer1() as f:
        sleep(5.5)

    with cm_timer2() as f1:
        sleep(1.2)


if __name__ == '__main__':
    main()
