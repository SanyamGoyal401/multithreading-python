import random as r
import threading

matrix_list = [[] for i in range(100)]


def task(startIndex, endIndex):
    for i in range(startIndex, endIndex + 1):
        mat = [[r.randint(0, 1000) for j in range(100)] for k in range(100)]
        matrix_list[i] = mat


activeThreads = threading.active_count()

t1 = threading.Thread(target=task, args=(0, 24))
t2 = threading.Thread(target=task, args=(25, 49))
t3 = threading.Thread(target=task, args=(50, 74))
t4 = threading.Thread(target=task, args=(75, 99))

t1.start()
t2.start()
t3.start()
t4.start()

while (threading.active_count() != activeThreads):
    pass
