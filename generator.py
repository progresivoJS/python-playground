import sys
import time


# intro to generator.
def Range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in Range(5):
    print(x)

# generator expression
# It's good for simple iteration.
a = [i for i in range(10) if i % 2]
b = (i for i in range(10) if i % 2)
print(a, b)


# Why generator?
# 1. effective memory use.
print(sys.getsizeof([i for i in range(100) if i % 2]))
print(sys.getsizeof([i for i in range(1000) if i % 2]))
print(sys.getsizeof((i for i in range(100) if i % 2)))
print(sys.getsizeof((i for i in range(1000) if i % 2)))

# 2. Lazy evaluation
def sleep_func(x):
    print("Sleep ...")
    time.sleep(1)
    return x

_list = [sleep_func(x) for x in range(5)]
for i in _list:
    print(i)

_generator = (sleep_func(x) for x in range(5))
for i in _generator:
    print(i)

# Exmaple : Fibonacci Sequence
def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1

fib = fibonacci(10)
for x in fib:
    print(x)
