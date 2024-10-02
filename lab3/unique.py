# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs and kwargs['ignore_case']:
            for i in range(len(items)):
                items[i] = str(items[i]).lower()
        self.items = set(items).__iter__()

    def __next__(self):
        return self.items.__next__()

    def __iter__(self):
        return self
