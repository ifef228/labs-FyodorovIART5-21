def print_result(func):
    def wrapper():
        print(func)
        result = func()
        print_decorated(result)

    return wrapper


def print_result_args(func):
    def wrapper(*arg):
        print(func)
        result = func(arg[0])
        print_decorated(result)

    return wrapper


def print_decorated(result):
    if type(result) is list:
        for x in result:
            print(str(x))
    elif type(result) is dict:
        for key in result:
            print(key + "=" + str(result[key]))
    else:
        print(result)


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]
