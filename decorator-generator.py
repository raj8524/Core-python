
"""
import collections

l=[1,2,3,4,6,7,8,9,2,4,5,6,20,40,11,5]
# l1=[(i,count) for i in collections.Counter(l) if count >2]
# print(l1)
z=[]
dict1={}
for i in l:
    dict1[i]=l.count(i)
for k,v in dict1.items():
    if v==1:
        z.append(k)
# print(sorted(z))
m=sorted(z).pop(len(z)-2)
print(m)

from numpy import *
from array import *
T=[[11,12,13,14],
   [15,16,17,18],
   [19,20,21,22],
   [23,24,25,26]]
# T.insert(3,[0,0,0,1])
# T=delete(T,s_[2],1)
# x=array('i',T)
# print(T)
# rez=[T[j][i] for j in T[i] for i in range(len(T[0]))]
# print("\n")
# for row in rez:
#     print(row,end=" ")
# print()
"""
T=[[11,12,13,14],
   [15,16,17,18],
   [19,20,21,22],
   [23,24,25,26]]
# T_matrix=map(list,zip(*T))
# for k in T_matrix:
#     print(list(k))
# import numpy
# print(numpy.transpose(T))

# print([list(x) for x in zip(*T)])
#
# y=list(map(list,zip(*T)))
# for i in y:
#     print(i)



import collections
from collections import Counter
# dict1=collections.OrderedDict()
# for i in range(10):
#     dict1[i]=i*i
# print(dict1)
# for item in dict1.items():
#     print(item,end=" ")
# l=[1,4,5,6,7,1,3,5,6,1,7,8,9,10]
# dict1={}
# for i in l:
#     dict1[i]=l.count(i)
# print(dict1)
# k=[(i, count) for i,count in collections.Counter(l).items() if count >1]
# print(k)
# # k=[(i,x) for i,x in enumerate(l) if i>2]
# k=[(i,c*])
# print(collections.OrderedDict([(i,i*i) for i in range(10)]))
# import math
# value=[]
# c,h=50,30
# items=[( value.append(str(round(math.sqrt(2*c*float(x)/h))))) for x in input("enter number" ).split(',')]
# print(items)
"""
#function passed as an argument
def square(x):
    return x * x
def my_map(func,*args):
    result=[]
    for i in args:
        result.append(func(i))
    return result
print(my_map(square,*[3,4,5,6]))
print(square)

#function returning fuction as first class function
def html_tag(tag):
    def wrap_text():
        print(tag)
    return wrap_text     #returning the inner function
print_h1=html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')




#function as an closure
def outer_func():
    message="hi"
    def inner_func():
        print(message)
    return inner_func()  #fucntion returning and executing as well
outer_func()


#decorator
def decorator_func(origional_func):
    def wrapper_func():
        print("new functionality is added")
        return origional_func()
    return wrapper_func
def display():
    print("dispaly fucntion run")
xy=decorator_func(display)
xy()

####---------------------ORRR   DECORATOR OTHER WAY
def decorator_func(origional_func):
    def wrapper_func():
        print("new functionality is added")
        return origional_func()
    return wrapper_func
@decorator_func
def display():
    print("dispaly fucntion run")
# xy=decorator_func(display)
# xy()
display()


#-----------------decorator examples
def decorator_func(origional_func):
    def wrapper_func(*args):
        print(f"new functionality is added for {origional_func.__name__}")
        return origional_func(*args)
    return wrapper_func
@decorator_func
def display():
    print("dispaly fucntion run")
@decorator_func
def display_info(name,age):
    print(f"dispaly_info ran {name},{age}")
display_info("raj",31)
display()
#

#---------------------decorator using class---
# def decorator_func(origional_func):
#     def wrapper_func(*args):
#         # print(f"new functionality is added for {origional_func.__name__}")
#         # return origional_func(*args)
#         pass
#     return wrapper_func

class decorator_class:
    def __init__(self,origional_func):
        self.origional_func=origional_func

    def __call__(self, *args, **kwargs):
        print(f"new functionality is added for {self.origional_func.__name__}")
        return self.origional_func(*args)

@decorator_class
def display():
    print("dispaly fucntion run")
@decorator_class
def display_info(name,age):
    print(f"dispaly_info ran {name},{age}")
display_info("raj",31)
display()

"""



l2=[]
l1=[3,5,6,7,'a']
def outer(func):
    def inner(args):
        [l2.append(i)for i in args if type(i)==int]
        print(l2)
        return func(l2)
    return inner

@outer
def letit(args):
    pass
letit(l1)





























































