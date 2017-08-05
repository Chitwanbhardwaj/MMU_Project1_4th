from threading import *
#Creating a thread for time Leap/interval
def hello():
    print "hello world"

t = Timer(10.0,hello)

t.start()