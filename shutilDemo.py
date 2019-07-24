import time
import os,shutil


if __name__ == '__main__':
    path = "/Users/qiansanshao/Downloads"
    dir = os.path.join(path,"abc")
    dst = os.path.join(path,"ddd")
    shutil.copytree(dir,dst)
    time.sleep(3)
    shutil.rmtree(dst)

