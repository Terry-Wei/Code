# coding:utf-8

import time, random

def show():
    start = time.time()
    while True:
        num = random.randint(0, 1000)
        if num == 200:
            print(time.time() - start)
            time.sleep(2)

if __name__=="__main__":
    show()


