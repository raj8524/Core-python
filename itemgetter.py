# from operator import itemgetter
#
# # Initializing list of dictionaries
# lis = [{"name": "Nandini", "age": 20},
#        {"name": "Manjeet", "age": 20},
#        {"name": "Nikhil", "age": 19}]
#
# # using sorted and itemgetter to print list sorted by age
# print "The list printed sorting by age: "
# print sorted(lis, key=itemgetter('age'))
#
# print ("\r")
#
# # using sorted and itemgetter to print list sorted by both age and name
# # notice that "Manjeet" now comes before "Nandini"
# print "The list printed sorting by age and name: "
# print sorted(lis, key=itemgetter('age', 'name'))
#
# print ("\r")
#
# # using sorted and itemgetter to print list sorted by age in descending order
# print "The list printed sorting by age in descending order: "
# print sorted(lis, key=itemgetter('age'), reverse=True)
#

# n = int(input())
# dict1 = {}
# marks = []
# query_name = input()
# for i in  range(0, n):
#     name = input()
#     for j in range(0, 3):
#         marks.append(j)
#     dict1["name"]=marks
#
# for key, values in dict1.items():
#     if query_name == key:
#         x=sum(values)/3
#         print(key,x)
#
# ################

# total = int(input())
# students = {}
# for x in range(total+1):
#     info = input().split()
#
#     key = info[0]
#     if key in students:
#         print('%.2f' % ((students[key][0] + students[key][1] + students[key][2]) / 3.00))
#     else:
#         students[info[0]] = [float(info[1]), float(info[2]), float(info[3])]

# elif (a.isspace())==True:
#             newstring+=a
#         elif a=='.':
#             newstring+=a
#         elif a == 2 :
#             newstring+=a

# s=input(" enter string : ")
# def change(x):
#     if str.islower(x):
#         return str.upper(x)
#     else:
#         return str.lower(x)
# def swap_case(s):
#     return ('').join(map(change,s))
# print(swap_case(s))

# a="xabababax"
# x="aba"
# count=0
# for i in range (len(a)):
#     if a[i:i+len(x)]==x:
#         count+=1
# print(count)
# S = input();
# ss = input();
# count = 0;
# a="xabababax"
# x="aba"
# count=0
# for i in range(0, len(a)):
#     count += a.count(x,i,i+len(x))
# print(count)

# s=input()
# t=type(s)
# for method in [t.isalnum, t.isalpha, t.isdigit, t.islower, t.isupper]:
#     print(any(method(c) for c in s))
#
# def mutate_string(string,position,k):
#     l=[]
#     l=list(string)
#     l[position]=k
#     string="".join(l)
#     return string
# print(mutate_string(s,position,k))


# import textwrap
# def wrap(string, max_width):
#     x=[]
#     x=textwrap.wrap(string,max_width)
#     y=[]
#     for i in x:
#         y.append(i)
#     return "\n".join(y)
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)


# def wrap(s1,width):
#     s = str
#     for i in s1(0, len(s1), width):
#
#         s+=s1[i:i+width]+"\n"
#     return s
# s1=input()
# width=5
# print(wrap(s1,width))
#
# for i in range(1, n + 1):
#     x = i
#     y = oct(i)
#     z = hex(i)
#     a = bin(i)
#     sep = len(a[1:]
#     print(str(i).rjust(sep, ' '), end=' ')
#     print(y.rjust(sep, ' '), end=' ')
#     print(z.rjust(sep, ' '), end=' ')
#     print(b.rjust(sep, ' '), end=' ')
n = int(input())
l = 2*n - 1 + 2*n - 2
for i in range(n-1):
    a = []
    for j in range(i):
        a.append(chr(ord('a')+n-1-j))
    u = list(reversed(a))
    a.append(chr(ord('a')+n-1-i))
    a += u
    print('-'.join(a).center(l, '-'))
































