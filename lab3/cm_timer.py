from time import time, sleep
from contextlib import contextmanager


class CmTimer1:
    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time() - self.start)


@contextmanager
def cm_timer2():
    start_time = time()
    yield
    end_time = time()
    print(end_time - start_time)



