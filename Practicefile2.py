import threading
import random

def list_append(List, count, id):
    for i in range(count):
        List.append(random.random())

if __name__ == "__main__":
    size = 512
    threads = 2
    jobs = []
    for i in range(0 , threads):
        List = list()
        thread = threading.thread(target=list_append(size, i, List))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print "list prepared"