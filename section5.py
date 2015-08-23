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
zipped = list(zip(x, y))
# print(zipped)

del zipped[1:2]

# print(zipped)

t = 12345, 54321, 'hello!'
x, y, z = t
# print(x)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)

# print('orange' in basket)

a = set('abracadabra')
b = set('alacazam')

# print(a - b)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
# print(tel)
# print(sorted(tel.keys()))
#
# print('guido' not in tel)


# for i in reversed(range(1, 10, 2)):
#     print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for f in sorted(set(basket)):
#     print(f)

words = ['cat', 'window', 'defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
# print(words)

string1, string2, string3 = '', 'Trndheim', 'Hammer Dance'
non_null = string1 or string2 or string3
# print(non_null)

# print((1, 2, 3) == (1, 2, 4))
# print('ABC' < 'C' < 'Pascal' < 'Python')

# print((1, 2, 3) == (1.0, 2.0, 3.0))
# print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
