#these r i/o bound task which doesnt perform much load on cpu i.e opening read,write file operations,network operation.
import time
start = time.perf_counter()
"""
def do_something():
    print(f'Sleeping 1 second(s)...')
    time.sleep(1)
    print('done sleeping ..')
do_something()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


#---------threading without arguments--------
import threading
def do_something():
    print(f'Sleeping 1 second(s)...')
    time.sleep(1)
    print('done sleeping ..')

threads=[]
for _ in range(10):    #running 10 threads
    t=threading.Thread(target=do_something)
    t.start()
    threads.append(t)
for thread1 in threads:
    thread1.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


#----threading with arguments-----------
import threading
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(1)
    print('done sleeping ..')
threads=[]
for _ in range(10):     #running 10 threads
    t=threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)
for thread1 in threads:
    thread1.join()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


#---M2---threading with concurrent module------------#######-------M2--------------------
import concurrent.futures
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(1)
    return 'done sleeping ..'

with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(do_something,1) for _ in range(10)]  #running 10 threads

    for f in concurrent.futures.as_completed(results):
        print(f.result())
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')


# ------M2--with concurrent module-----------
import concurrent.futures
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(1)
    return 'done sleeping ..'

with concurrent.futures.ThreadPoolExecutor() as executor:
    seco=[5,3,4,2,1]
    results=[executor.submit(do_something,sec) for sec in seco]  #running 10 threads

    for f in concurrent.futures.as_completed(results):
        print(f.result())
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')

"""

#--------M2---concurrent module with map func---------
import concurrent.futures
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    x=10
    time.sleep(1)
    return f'done sleeping ..{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    seco=[5,3,4,2,1]
    results=executor.map(do_something,seco)

    for result in results:
        print(result)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')