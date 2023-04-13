import math
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
import urllib.request


values = [12,20,4,100,64,77,200,9,10]

def mycosine(n):
    return math.cos(n)

def concurrent_cosines():

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_val = {executor.submit(mycosine, val, 60): val for val in values}
        for future in concurrent.futures.as_completed(future_to_val):
            for val in values:
                res = mycosine(val)
                print('Cosine of %s is %s' % (val,res), '\n')

concurrent_cosines()


if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("concurrent_cosines()", setup="from __main__ import concurrent_cosines", number=2)/2             
    print(elapsed_time) 