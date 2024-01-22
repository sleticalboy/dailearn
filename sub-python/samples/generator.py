import math
import time


def timer(fn):
    def _pow(*args, **kwargs):
        start = time.time()
        r = fn(*args, **kwargs)
        print(f'cost: {(time.time() - start) * 1e3}s')
        return r

    return _pow


def powers(num):

    @timer
    def _pow(x, y):
        return math.pow(x, y)

    for i in range(num):
        # 生成器
        yield int(_pow(i, 3))


def run_main():
    for n in powers(11):
        print(n, end=', ')
    print()
    print(type(powers(11)), powers(11))
    pass


if __name__ == '__main__':
    run_main()
    pass
