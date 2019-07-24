import multiprocessing
import os
import time


def worker(name):
    print(name," is hardworking on pid ",os.getpid())
    time.sleep(5)


if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    p1 = multiprocessing.Process(target=worker,args=("sanshao",))
    p2 = multiprocessing.Process(target=worker,args=("zhangsan",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("main process end")