# Generator functions allow you to declare a function that behaves like an iterator.

# An iterator is an object that can be iterated (looped) upon. It is used to abstract a container of data to make it behave like an iterable object.

a = (i for i in range(5))
b = iter([1,2,3,4])
print(a) # a is generator
print(b) # b is iterator

# Lazy evaluation is an evaulation strategy which delays the evaluation of an expression until its value is needed and which also avoids repeated evaluations.