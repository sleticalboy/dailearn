import math
import multiprocessing
import os
import time


def task_proc(q: multiprocessing.Queue, max_):
    print(f'task_proc() started pid: {os.getpid()} -> {time.time()}')
    while 1:
        msg = q.get()
        print(f'task_proc() msg type: {type(msg)} -> {msg}')
        if msg == max_:
            break
        time.sleep(0.2)
        pass
    print(f'task_proc() exit pid: {os.getpid()}')
    pass


def run_main():
    q = multiprocessing.Queue()
    max_ = 10
    proc = multiprocessing.Process(target=task_proc, name='test-proc', daemon=True, args=(q, max_))
    proc.start()
    print(f'run_main() pid: {os.getpid()} -> {time.time()}')

    for i in range(1, max_ + 1, 1):
        time.sleep(0.1)
        q.put(i * math.pi)
        time.sleep(0.1)
        q.put('hello ' * i)
        time.sleep(0.1)
        q.put(i)
        print(f'run_main() {i}')
    proc.join()
    pass


if __name__ == '__main__':

    from tee import Tee

    run_main()
    pass
