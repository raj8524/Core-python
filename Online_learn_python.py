# str1="xyzrt"
# str2=str()
# for i in  range (1,len(str1)+1):
#     str2+=str1[-i]
#
#
#     # str2+=(str1[::-i])
# print(str2)
#
# z=0
# l1=[2,5,10,8,9]
# for i in l1:
#     if i<i+1 :
#         z=i
#     else:
#          print("go to next number")
# print(z)


# l1=[65,21,34,987,0,8]
# min1=l1[-2]

# for i in l1:
#
#     if i<min1:
#         min1=i

# print(min1)
# m=l1[2]
# for i in range(1,len(l1)):
#     if l1[i] < m:
#        m=l1[i]
#     print(l1)


# min1=l1[3]
# #
# l=[min1 for i in l1 if (i<min1)]
# print(l)

# y=frozenset(x for x in range(20) if x%2 !=0 or x%5==0)
# print(y)



# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
#
# m={key:value for key,value in zip(state,capital)}
# print(m)

# l1=[65,21,34,987,0,8]
# m=l1[2]
# for i in range(1,len(l1)):
#     if l1[i] < m:
#        m=l1[i]
# print(l1)


#
# def sum1(n):
#     temp=0
#     add1=0
#     temp=n%10
#
#     add1=add1+temp
#     n = n // 10
#     print(add1)
#
#     if add1 >0 and add1 <9:
#         return add1
#     else:
#         sum1(add1)
#
# n=int(input("enter number :"))
# print(sum1(n))
#
#


# def sum_number_1_method(n):
#     sum = 0
#     while (n>0):
#         res = n % 10
#         sum = sum + res
#         n = n // 10
#
#     return sum if sum < 10 else sum_number_1_method(sum)
# num=int(input("enter number : "))
# print("2nd result : ", sum_number_1_method(num))
"""
def inpi():
    l1=[4,1,5,2,9,85,0]
    for j in range(len(l1)-1):
        for i in range(len(l1)-1):
            if l1[i]>l1[i+1]:
                l1[1],l1[i+1]=l1[i+1],l1[i]
    print("bubble sorting in ascending order:" ,l1)
__name__== '__main__'
# print(inpi())

                     # occurance of character in string
str1="raj kumar "
duplicate={}
for i in str1:
    if i in duplicate:
        duplicate[i]+=1
    else:
        duplicate[i]=1
for key,value in duplicate.items():
    print(f"{key} is present {value}")



import math
x=5
print(math.remainder(x,3))

# febonacci
l1=[]
def febo(num):
    a,b,temp=0,1,0
    for i in range(1,num):
        l1.append(temp)
        a=b
        b=temp
        temp=a+b

    return l1
# print(febo(7))
# def prime(list(febo(7))) :
def prime():
    l2=[]
    l2=febo(7)
    print(l2)
    # for i in l2:
    #     if i>1:
    #         for j in range(2,i):
    #             if i%j==0:
    #                 print("its not prime number")
    #                 break
    #         else:
    #             print(f"{i} its  prime number")
    #     else:
    #         print(f"{i} its not  prime number")
    for i in l2:
        flag=0
        for j in range(2, i):
            if (i%j == 0):
                print('%d is not a prime number',i)
                flag = 0
                break
        if (flag == 1):
            print('%d is a prime number',i)
prime()


# list of prime numbers
# def primenumber(limit):
#     for j in range (2,limit):
#         for i in range(2,j):
#             if j%i == 0 :
#                 break
#         else:
#             print(j)
# x=int(input("enter number :"))
# primenumber(x)

def Prime_Number():
    flag = 1
    n = int(input('Enter the number'))
    for i in range(2,n):
        if(n%i == 0):
            print('its not a prime number',n)
            flag = 0
            break
    if(flag == 1):
        print('its a prime number',n)
Prime_Number()


# guess game
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("guess : "))
    guess_count+=1
    if guess==secret_number:
        print("Hurrey u won !")


                 #################          car Game
# car_game=""
# started=False
# while True:
#     car_game=input("> ")
#     if car_game.lower() == "start":
#         if started:
#             print("car already started")
#         else:
#             started=True
#             print("car started....")
#     elif car_game.lower() == "stop":
#
#         if not started:
#             print("car already stopped")
#         else:
#             print("stop the car")
#     elif car_game=="help":
#         print("""
#         start-to start the car
#         stop-to stop car
#         quit-to quit the game
#         """)

"""                                                              
#m1     
*****
**
*****
**
**
i=1
while i<=4:                                       
    if i%2!=0:
        print("*"*5)
        i+=1
    else:
        print("*" * 2)                                                                                                                                                            
        i += 1
print("*" * 2)
#m2
y=[5,2,5,2,2]
for i in y:
    output=""
    for j in range(i):
        output+='x'
    print(output)    

emoji={
    "sad":"😌",
    "happy":"🥰"
}
print(f"i m  {emoji.get('happy')}")



import random
# dice=range(1,7)
# print(f"{random.choice(dice)},{random.choice(dice)}")
class dice:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def roll(self):
        return self.x,self.y

    
x=random.randint(1,6)
y=random.randint(1,6)
Dice=dice(x,y)
print(Dice.roll())

import calendar
print(calendar.weekheader(2))
print(calendar.month(2020,2))


k=list()

for i in l:
    k.append(i+" i dump u")
print(k)

l=['ritu','madhuri',"priyanka"]
print([person + " i dump u" for person in l])


# regex
import re
text="random string. kraj6250@gmail.com some more . raj.raj92120@gmail.net"
pattern=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
result=pattern.search(text)  # gives only first one
print(result)
result=pattern.findall(text)  # gives all mail id
print(result)


import datetime
today=datetime.date.today()
# today=datetime.time.hour
# print(today)
birthday=datetime.date(1992,1,20)
days_since_birth=(today-birthday).days
# print(days_since_birth)
hour_delta=datetime.timedelta(hours=10)
# print(datetime.datetime.now())
# print(datetime.datetime.now()+hour_delta)
print(datetime.datetime.now().strftime('%B %d,%Y'))
print(datetime.datetime.now().strptime('March 09,2019','%B %d,%Y'))

######------------------Zip func---------
l1=[1,2,3,4,5]
l2=['one','two','three','four','five']
zipped=list(zip(l1,l2))
# print(zipped)
unzipped=list(zip(*zipped))  #unpacking
# print(unzipped)

for (i,j) in zip(l1,l2):
    print(i,j)




iseven=lambda x:x%2==0
print(iseven(*x))
x=[6,7,8,20]

slicing=lambda x:x[:3]
print(slicing("abcd"))

dic1={
    "name":"raj",
    "id":"4500",
    "profile":"developer"

}

m={k:v+"rocking" for k,v in dic1.items()}
print(m)


                        # enumerate
# name1=["raj","is",'awesome']
name1="abcde"
for i,k in enumerate(name1):
    print(f"position is {i} of {k}")
                                # dictionary comprehension
print({f"position is {j}": name1[j] for j in range(0,len(name1))})
# print(pos)

num1=[5,9,33,8]
print(list(map(lambda a:a*2,num1)))


names={'raj',"ankita","ravi","raunak"}
ages=(29,25,23,20)
print(dict(zip(names,ages)))

"""
avg=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(avg([2,3,46],[4,6,8],[8,10,20]))

















































































































































































