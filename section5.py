__author__ = 'n00b'

# l = [1, 2, 3]
# l[len(l):] = [4]

from collections import deque

queue = deque(["Eric", "john", "Micheal"])
queue.append("Terry")
queue.append("Graham")
# print(queue.popleft())

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
# print(squares)

l = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

vec = [-4, -2, 0, 2, 4]

l = [(x, x**2) for x in vec]

vec = [[1,2,3], [4,5,6], [7,8,9]]
l = [x for y in vec for x in y]

from math import pi
l = [str(round(pi, i)) for i in range(1, 6)]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

l = [[row[i] for row in matrix] for i in range(4)]

# print(l)


x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))

print(list(zip(*zip(x, y))))

x2, y2 = zip(*zip(x, y))
print(x == list(x2) and y == list(y2))

