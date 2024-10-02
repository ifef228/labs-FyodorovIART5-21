import json
import random

from cm_timer import CmTimer1
from field import field
from lab3.decorator import *
from unique import Unique

path = "data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result_args
def f1(arg):
    return sorted(Unique(field(arg, "job-name"), ignore_case=True).items)


@print_result_args
def f2(arg):
    return list(filter(lambda value: value is not None and str(value).startswith('программист'), arg))


@print_result_args
def f3(arg):
    return list(map(lambda value: (str(value) + " с опытом Python"), arg))


@print_result_args
def f4(arg):
    return list(map(lambda value: value[0] + ", зарплата " + str(value[1]),
                    zip(arg, [random.randint(100_000, 200_000) for _ in range(len(arg))])))


if __name__ == '__main__':
    with CmTimer1():
        f4(f3(f2(f1(data))))
