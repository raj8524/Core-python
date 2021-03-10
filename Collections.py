"""
import collections
from collections import Counter

y=[item for item,count in Counter(x).items() if count>1]
# print(Counter(["e","z","u","z","E","a","F"]))
y=sorted(y,reverse=True)
print(y)


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

# Accessing Values using key name
print(c['a'])

# Accesing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())

from collections import defaultdict
x=["e","z","u","z","e","a","F"]
L = [1, 2, 3, 4, 2, 4, 1, 2]
d=defaultdict(str)
for i in x:
    d[i]+=1
print(d)


from collections import deque
de=deque([3,4,5])
de.append(8)
de.appendleft(1)
print(de[3])
"""

class x:
    def __init__(self):
        pass
    def xy(self):
        print(__name__)
z=x()
z.xy()





















































































