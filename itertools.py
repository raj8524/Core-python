import itertools
# counter=itertools.count()
# data=[100,200,300,400,800]
# print(list(zip(itertools.count(),data)))
# print(list(zip(itertools.count(start=5,step=-2.5),data)))
# print(list(zip(range(10),data)))
# print(list(itertools.zip_longest(range(10),data)))

# counter1=itertools.cycle(('on','off'))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))
# print(next(counter1))


# counter=itertools.repeat(2,times=3)
# squares=map(pow,range(10),itertools.repeat(3))
# print(list(squares))

# counter=itertools.starmap(pow,[(0,2),(2,3),(4,5)])
# print(list(counter))

letters = ['a', 'b', 'c', 'd']
numbers = [2, 1, 2, 3,2,10,0]
names = ['Corey', 'Nicole']
# result=itertools.combinations(letters,3)
# for item in result:
#     print(item)
# result=itertools.permutations(letters,3)
# for item in result:
#     print(item)

# result=itertools.product(numbers,repeat=3)
# for item in result:
#     print(item)

# result=itertools.combinations_with_replacement(numbers,3)
# for item in result:
#     print(item)

# combined=itertools.chain(letters,numbers,names)
# for item in combined:
#     print(item)

# result=itertools.islice(range(10),1,5,2)   #rnage,start,end,step
# for item in result:
#     print(item)

#
# with open("log.txt")as f:
#     header=itertools.islice(f,3)
#     for line in header:
#         print(line,end="")

# selectors=[True,True,False,True]
# result=itertools.compress(letters,selectors)
# for item in result:
#     print(item)

# def lt_2(n):
#     if n<2:
#         return True
#     return False
# # result=filter(lt_2,numbers)
# result=itertools.filterfalse(lt_2,numbers)
# for item in result:
#     print(item)

# def lt_2(n):
#     if n<2:
#         return True
#     return False
# # result=filter(lt_2,numbers)
# result=itertools.dropwhile(lt_2,numbers)
# for item in result:
#     print(item)

# def lt_2(n):
#     if n<2:
#         return True
#     return False
# # result=filter(lt_2,numbers)
# result=itertools.takewhile(lt_2,numbers)
# for item in result:
#     print(item)

# result1=itertools.accumulate(numbers)
# for item in result1:
#     print(item)

# result1=itertools.accumulate(enumerate(numbers))
# for item in result1:
#     print(item)

# import operator
# result1=itertools.accumulate(numbers,operator.mul)
# for item in result1:
#     print(item)

"""

def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)

for key, group in person_group:
    print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()
"""



















