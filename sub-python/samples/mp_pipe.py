import logging
import math
import random
from multiprocessing import Pipe, Process
import os
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


def task_proc(cc):
    pid = os.getpid()
    logging.info(f'task_proc() started pid: {pid} -> {time.time()}')
    while 1:
        msg = cc.recv()
        logging.info(f'task_proc() recv msg: {type(msg)} -> {msg}, pid: {pid}')
        if msg == 'quit!':
            break
        time.sleep(random.uniform(0.1, 0.4))
        cc.send(f'{msg} ack')
        pass
    logging.info(f'task_proc() exit pid: {os.getpid()}')
    pass


def run_main():
    pc, cc = Pipe(duplex=True)
    proc = Process(target=task_proc, name='test-proc', daemon=True, args=(cc,))
    proc.start()
    logging.info(f'run_main() pid: {os.getpid()} -> {time.time()}')

    for i in range(1, 11, 1):
        pc.send(i * math.pi)
        time.sleep(random.uniform(0.1, 0.5))
        msg = pc.recv()
        logging.info(f'run_main() recv msg: {type(msg)} -> {msg}')
    pc.send('quit!')
    proc.join()
    pass


if __name__ == '__main__':
    run_main()
    pass
