class Range:
    def __init__(self, n):
        self.n = n
        self.c = 0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.c < self.n:
            v = self.c
            self.c += 1
            return v
        else:
            raise StopIteration

class RangeFactory:
    def __init__(self, n):
        self.n = n
        self.c = 0
    
    def __iter__(self):
        return Range(self.n)

# Range
for x in Range(3):
    print(x)

it = iter(Range(3))
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

# RangeFactory
for x in RangeFactory(3):
    print(x)

it = iter(RangeFactory(3))
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

# Caveat
print("Caveat")
r = Range(3)
for x in r:
    print(x)
    if x == 1:
        break

for x in r:
    print(x)

r = RangeFactory(3)
for x in r:
    print(x)
    if x == 1:
        break

for x in r:
    print(x)