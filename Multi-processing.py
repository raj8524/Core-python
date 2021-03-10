import multiprocessing
import time
start=time.perf_counter()
"""
def do_something():
    print('sleeping 1 second..')
    time.sleep(1)
    print('Done sleeping...')

p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=do_something)
p1.start()
p2.start()
p1.join()
p2.join()
finish=time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds')

#----multiple process in loop------
def do_something():
    print('sleeping 1 second..')
    time.sleep(1)
    print('Done sleeping...')
process=[]
for _ in range(10):
    p=multiprocessing.Process(target=do_something)
    p.start()
    process.append(p)

for pro in process:
    pro.join()
finish=time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds')

#--------------with concurrent futures-------------
import concurrent.futures
def do_something(seconds):
    print('sleeping 1 second. {seconds}.')
    time.sleep(1)
    return 'Done sleeping...'
with concurrent.futures.ProcessPoolExecutor() as executor:
    f1=executor.submit(do_something,1)
    print(f1.result())

finish=time.perf_counter()
print(f'finished in {round(finish-start,2)} seconds')

#--------------with concurrent futures with multiple process ------------
import concurrent.futures
def do_something(seconds):
    print('sleeping 1 second. {seconds}.')
    time.sleep(1)
    return 'Done sleeping...'
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results=[executor.submit(do_something,1) for _ in range(10)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

if __name__=="__main__":
    main()
    finish = time.perf_counter()
    print(f'finished in {round(finish - start, 2)} seconds')



#-------------with multiple different time process with map function -------
import concurrent.futures
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)

if __name__=="__main__":
    main()
    finish = time.perf_counter()
    print(f'finished in {round(finish - start, 2)} seconds')
"""

#-----------------------
import concurrent.futures
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'
def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results =[executor.submit(do_something,sec) for sec in secs]
        for f in concurrent.futures.as_completed(results):
            print(f.result())
if __name__=="__main__":
    main()
    finish = time.perf_counter()
    print(f'finished in {round(finish - start, 2)} seconds')








