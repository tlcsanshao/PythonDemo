import multiprocessing
import os
import time


def worker(name):
    print(name," is hardworking on pid ",os.getpid())
    time.sleep(5)


if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    p = multiprocessing.Pool()
    p.apply_async(worker,args=("sanshao",))
    p.apply_async(worker,args=("zhangsan",))
    p.close()
    p.join()
    print("main process end")