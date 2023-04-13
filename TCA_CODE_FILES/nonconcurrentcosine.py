import math

values = [12,20,4,100,64,77,200,9,10]

def mycosine(n):
    return math.cos(n)

def non_concurrent_cosines():
    for val in values:
        res = mycosine(val)
        print('Cosine of %s is %s' % (val,res), '\n')

non_concurrent_cosines()

if __name__ == '__main__':
    import timeit
    elapsed_time = timeit.timeit("non_concurrent_cosines()", setup="from __main__ import non_concurrent_cosines", number=2)/2             
    print(elapsed_time)