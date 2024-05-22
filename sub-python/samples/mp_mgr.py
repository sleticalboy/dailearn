import logging
import math
import random
from multiprocessing import Process, Manager
import os
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def task_proc(sl, sd):
    pid = os.getpid()
    logging.info(f'task_proc() started pid: {pid} -> {time.time()}')
    while True:
        msg = sl[len(sl) - 1]
        logging.info(f'task_proc() recv msg: {type(msg)} -> {msg}, pid: {pid}')
        if msg == 'quit!':
            break
        sd['idx'] = f'{msg:.2f}'
        time.sleep(random.uniform(0.1, 0.4))
        pass
    logging.info(f'task_proc() exit pid: {os.getpid()}')
    pass


def run_main():
    # 管理器对象
    with Manager() as mgr:
        # 共享内存变量
        sl = mgr.list()
        sd = mgr.dict()

        proc = Process(target=task_proc, name='test-proc', daemon=True, args=(sl, sd))
        proc.start()
        logging.info(f'run_main() pid: {os.getpid()} -> {time.time()}')

        for i in range(1, 11, 1):
            sl.append(i * math.pi)
            time.sleep(random.uniform(0.1, 0.5))
            logging.info(f"run_main() idx: {sd['idx']}")
        sl.append('quit!')
        proc.join()

        # 手动销毁
        # mgr.shutdown()
        # 在 with 代码块中自动销毁
        pass
    pass


if __name__ == '__main__':
    run_main()
    pass
