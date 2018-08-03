# Define __str__ in a class to show a human-readable representation.

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)

p = Point(1, 2)
print(p)