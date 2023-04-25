"""
count é um iterador sem fim (itertools)
"""
from itertools import count

c1 = count(10, 8)
r1 = range(10, 100, 8)

print('Count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('Range')
for x in r1:
    print(x)