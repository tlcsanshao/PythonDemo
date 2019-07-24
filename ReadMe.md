### 一、pip的使用
1. 安装
2. pip list
3. pip freeze > myinstall.txt 

### 二、常用模块和用法

#### tqdm模块实现进度条功能
1.简单用法
```
    from tqdm import tqdm,trange
    import time
    
    for i in tqdm(range(100)):
        time.sleep(0.01)
    
    for i in trange(100):
        time.sleep(0.01)
        
    for i in tqdm(list("abcdefgij"),desc="字母处理",unit="字母"):
        time.sleep(1.2)
    
```
2.手动控制
```
    from tqdm import tqdm,trange
    import time
    
    process = tqdm(total=50)
    for i in range(10):
        time.sleep(0.5)
        process.update(5)
    process.close()
    # update的值为增加的值，增加的值总和要等于total
```
#### time模块
* time.sleep(0.2)
* time.time()
#### os模块
1.walk
```
import os

if __name__ == '__main__':
    path = "/Users/qiansanshao/Downloads"
    for root,folder,filename in os.walk(path):
        print(root,"--",folder,"--",filename)
# 从path开始，先找出path下所有的文件夹和文件，再依次遍历所有的文件夹
```
2.参数
```
print(os.name)
print(os.getpid())
print(os.getppid())
print(os.getcwd())

print(os.path.isdir(path))
print(os.path.isfile(path))
print(os.path.exists("osDemo.py"))
print(os.path.abspath("osDemo.py"))
print(os.path.join(os.getcwd(),"fab.txt"))

os.remove(os.path.join(path,"ReadMesss.md"))
```
#### shutil模块
1. shutil可以跟os一起使用。shutil比较擅长做文件的复制和删除
2. 常用操作
```
shutil.copy(src,dst)
shutil.copy2(src,dst)
shutil.copyfile(src,dst)
shutil.move(src,dst)
shutil.copytree(src,dst)
shutil.rmtree(src,dst)
```
#### multiprocessing实现多进程编程
1.Process开启子进程
```
import multiprocessing
import os
import time

def worker(name):
    for i in range(5):
        print(name," is hardworking on pid ",os.getpid())
        time.sleep(1)


if __name__ == '__main__':
    print(multiprocessing.cpu_count())
    p1 = multiprocessing.Process(target=worker,args=("sanshao",))
    time.sleep(0.5)
    p2 = multiprocessing.Process(target=worker,args=("zhangsan",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("main process end")
```
2.Pool进程池开启子进程
```
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
```
2.manager:用作各个进程之间共享数据对象


#### 常用的写法
* list(range(1,10,2))
> range(stop)
> range(start,stop[,step])
* 

