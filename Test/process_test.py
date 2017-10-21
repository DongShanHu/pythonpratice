#queue

##import multiprocessing as mp
##
##def job(q):
##    res = 0
##    for i in range(1000):
##        res += i+i**2+i**3
##    q.put(res) # queue
##
##if __name__ == '__main__':
##    q = mp.Queue()
##    p1 = mp.Process(target=job, args=(q,))
##    p2 = mp.Process(target=job, args=(q,))
##    p1.start()
##    p2.start()
##    p1.join()
##    p2.join()
##    res1 = q.get()
##    res2 = q.get()
##    print(res2)

#效率對比 multithreading, multiprocessing
##import multiprocessing as mp
##import threading as td
##import time
##
##
##
##def job(q):
##    res = 0
##    for i in range(1000000):
##        res += i+i**2+i**3
##    q.put(res) # queue
##
##def multicore():
##    q = mp.Queue()
##    p1 = mp.Process(target=job, args=(q,))  
##    p2 = mp.Process(target=job, args=(q,))
##    p1.start()
##    p2.start()
##    p1.join()
##    p2.join()
##    res1 = q.get()
##    res2 = q.get()
##    print('multicore:' , res1+res2)
##
##def normal():
##    res = 0
##    for _ in range(2):
##        for i in range(1000000):
##            res += i+i**2+i**3
##    print('normal:', res)
##
##def multithread():
##    q = mp.Queue()
##    t1 = td.Thread(target=job, args=(q,))
##    t2 = td.Thread(target=job, args=(q,))
##    t1.start()
##    t2.start()
##    t1.join()
##    t2.join()
##    res1 = q.get()
##    res2 = q.get()
##    print('multithread:', res1+res2)
##
##if __name__ == '__main__':
##    st = time.time()
##    normal()
##    st1= time.time()
##    print('normal time:', st1 - st)
##    multithread()
##    st2 = time.time()
##    print('multithread time:', st2 - st1)
##    multicore()
##    print('multicore time:', time.time()-st2)


#进程池 pool
##import multiprocessing as mp
##
##def job(x):
##    return x*x
##    
##def multicore():
####    process=mp.Process
##    pool = mp.Pool(processes=2)## 用到核的數量
##    res = pool.map(job, range(10))
##    print(res)
##    res = pool.apply_async(job, (2,))#job和一個值對應起來
##    print(res.get())
##    multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
##    print([res.get() for res in multi_res])
##
##if __name__ =='__main__':
##    multicore()


#共享內存
import multiprocessing as mp

value=mp.Value('d',1) #i 整數 d 小數
array=mp.Array('i',[1,2,3]) ##只能是1維的
