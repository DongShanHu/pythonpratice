##python threading
#多線層可以分批量做很多事，節省computing time)
import threading
import time
import copy
from queue import Queue 
def main():
    print(threading.active_count())

if __name__=='_main_':
    main()
##def thread_job():
##    print('T1 start\n')
##    for i in range(10):
##        time.sleep(0.1)
##    print('t1 finish \n')
##
##def T2_job():
##    print('T2 start \n')
##    print('T2 finish\n')
##    
##def main():
##    added_thread=threading.Thread(target=thread_job,name='t1') #定義了thread
##    thread2=threading.Thread(target=T2_job,name='t2')
####    print(threading.active_count())
####    print(threading.enumerate())
####    print(threading.current_thread) #主線層
##    added_thread.start() #運行thread
##    thread2.start()
##    thread2.join() #join以後的都要等待T1 或 all done運行完
##     added_thread.join()
##    print('all done \n')



#加入queue
##def job(l,q):
##    for i in range(len(l)):
##        l[i] = l[i]**2
##    q.put(l)
##
##def multithreading():
##    q = Queue()
##    threads = []
##    data= [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
##    for i in range(4):
##        t = threading.Thread(target=job, args=(data[i], q))
##        t.start()
##        threads.append(t)
##    for thread in threads:
##        thread.join()
##    results = []
##    for _ in range(4):
##          results.append(q.get())
##    print(results)
##
##if __name__ == '__main__':
##    multithreading()

#GIL 不一定有效率

##def job(l, q):
##    res = sum(l)
##    q.put(res)
##
##def multithreading(l):
##    q = Queue()
##    threads = []
##    for i in range(4):
##        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
##        t.start()
##        threads.append(t)
##    [t.join() for t in threads]
##    total = 0
##    for _ in range(4):
##        total += q.get()
##    print(total)
##
##def normal(l):
##    total = sum(l)
##    print(total)
##
##if __name__ == '__main__':
##    l = list(range(1000000)) 
##    s_t = time.time()
##    normal(l*4) #列表擴大4倍
##    print('normal: ',time.time()-s_t)
##    s_t = time.time()
##    multithreading(l)
##    print('multithreading: ', time.time()-s_t)

#lock
'''
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()
def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()

if __name__ == '__main__':
    lock=threading.Lock()
    A=0 #全局變量，共享內存
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
''''

