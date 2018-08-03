# star(*) operator can be used only in python3.
# It's used on the left hand side of an assignment to represent the rest of a sequence.
some_list = ['a', 'b', 'c', 'd', 'e']

(first, second, *rest) = some_list
print(rest)

(first, *middle, last) = some_list
print(middle)

(*head, penultimate, last) = some_list
print(head)


# use tuples to unpack data
values = ['dog', 'Fido', 10]
animal, name, age = values
print(animal, name, age)

# use _ as a placeholder for data in a tuple that should be ignored.
(name, age, _, _) = ['Jin', 25, 'M', 'Yonsei']
if age > 21:
    output = '{name} can drink!'.format(name = name)
    print(output)

# swap function using tuple
foo = 'Foo'
bar = 'Bar'
foo, bar = bar, foo
print(foo, bar)

