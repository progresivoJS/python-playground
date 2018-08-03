# Understanding List Comprehensions

# List Comprehensions
# list_variable = [x for x in iterable]
print("\nList Comprehensions")

shark_letters = [letter for letter in 'shark']
print(shark_letters)

# Using Conditionals with List Comprehensions
print("\nUsing Conditionals with List Comprehensions")
fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

fish_list = [fish for fish in fish_tuple if fish != 'octopus']
print(fish_list)

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

# It first check x % 3 == 0. if True, then it will check x % 5 == 0.
nested_number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(nested_number_list)


# Nested Loops in a List Comprehension
print("\nNested Loops in a List Comprehension")

my_list = []
for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)

print(my_list)

nested_my_list = [x * y for x in [20, 40, 60] for y in [2, 4, 6]]
print(nested_my_list)

# Conclusion
# It is a succint way of making list, but readability always takes precedence.
# It is concered with set-builder notation or set comprehension.