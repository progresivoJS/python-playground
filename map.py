def func(x):
    return x * 2

it = map(func, [1, 2, 3])
print(next(it))
print(next(it))
print(next(it))

# In python3, map() returns iterator.