import os

if __name__ == '__main__':
    path = "/Users/qiansanshao/Downloads"
    # for root,folder,filename in os.walk(path):
    #     print(root,"--",folder,"--",filename)

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