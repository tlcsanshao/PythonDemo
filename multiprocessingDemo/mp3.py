import multiprocessing,time


def reader(d):
    while True:
        time.sleep(1)
        print(d)


def writer(d):
    d["abc"] = 123

if __name__ == "__main__":

    manager = multiprocessing.Manager()   #生成Manager 对象
    d = manager.dict()   #生成共享dict

    jobs = []
    # p1 = multiprocessing.Process(target = reader,args=(d,))
    # p1.start()
    # jobs.append(p1)
    #
    # time.sleep(10)
    #
    # p2 = multiprocessing.Process(target = writer,args=(d,))
    # p2.start()
    # jobs.append(p2)
    #
    #
    # for p in jobs:
    #     p.join()

    pool = multiprocessing.Pool()
    pool.apply_async(reader,args=(d,))
    time.sleep(10)
    pool.apply_async(writer,args=(d,))

    pool.close()
    pool.join()

    print("end loop")