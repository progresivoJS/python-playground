# * operator can be used only in python3.
# It's used on the left hand side of an assignment to represent the rest of a sequence.
some_list = ['a', 'b', 'c', 'd', 'e']

(first, second, *rest) = some_list
print(rest)

(first, *middle, last) = some_list
print(middle)

(*head, penultimate, last) = some_list
print(head)