import random


def gen_random(num_count, begin, end):
    result = []
    for i in range(num_count):
        result.append(random.randint(begin, end))
    return result


