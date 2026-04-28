import time

def c_to_f(c):
    return c*9.0/5 +32

def my_sum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total

def square(n):
    sqsum = 0
    for i in range(n):
        for j in range(n):
            sqsum += i*i
    return sqsum

def time_wrapper(f, L):
    print('Timing',f.__name__)
    for i in L:
        t = time.time()
        f(i)
        dt = time.time() - t
        print(f"{f.__name__}({i}) took {dt} seconds")

L_N = [1]

for i in  range(4):
    L_N.append(L_N[-1]*10)

time_wrapper(c_to_f, L_N)
time_wrapper(my_sum, L_N)
time_wrapper(square, L_N)