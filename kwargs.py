# Understanding *args.
print("\nUnderstanding *args")

def multiply(a, b):
    '''
    return a * b
    there is limit that there is fixed number of paramters.
    '''
    print(a * b)

def multiply_with_args(*args):
    '''
    return multiplication of args.
    '''
    res = 1
    for i in args:
        res *= i
    print(res)

multiply_with_args(3, 4, 5)
multiply_with_args(4, 5, 8, 9)
multiply_with_args(3, 4, 5, 6, 8, 9)

# Understading **kwargs
print("\nUnderstanding **kwargs")

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3 = True)

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name="Casey")
print_values(
    name_1="Alex",
    name_2="Gray",
    name_3="Jin",
    name_4="Hyeyoung",
    name_5="Yuna"
)

# Ordering Arguments
print("\nOrdering Arguments")
# 1. Formal Positional arguments
# 2. *args
# 3. Keyword arugments
# 4. **kwargs

def example(a, b, *args, **kwargs):
    pass

def example2(a, b, *args, kw_1, kw_2="blobfish", **kwargs):
    print(a, b)
    print(args)
    print(kw_1, kw_2)
    print(kwargs)

example2(1, 2, 5, 6, 8, 9, kw_1="shark", new_args="hello world")


# Using *args and **kwargs in Function Calls
print("\nOrdering Arguments")

def some_args(arg_1, arg_2, arg_3):
    print(arg_1, arg_2, arg_3)

args = ("Sammy", "Casey", "Alex")
some_args(*args)

args2 = [2, 3]
some_args(1, *args2)

def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

kwargs = {
    "kwarg_1" : "Val",
    "kwarg_2" : "Harper",
    "kwarg_3" : "Remy"
}

some_kwargs(**kwargs)

