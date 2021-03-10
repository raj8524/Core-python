#-------------------------------------OOP###############################------------------------------------------------
"""
class computer:
    laptop="HP"                   #class namespace    .static/class variable
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram               #instance namespace
        self.processor="intel"

    def config(self):
        print("config is", self.cpu,self.ram)

    def compare(self,comp2):
        if self.ram==comp2.ram:
            return True
        else:
            return False
comp1= computer('i7',16)
comp2= computer('invidia',8)
comp2.ram=64
comp1.config()
comp2.config()
#comp2.laptop="lenovo"    #changed using object name
computer.laptop="mi"   #changed using class name
print(id(comp1))
print(comp1.processor,comp1.laptop)
print(comp2.processor,comp2.laptop)
if comp1.compare(comp2):
    print("they r same")
else:
    print("they r different")
"""
#size of an object depends on the number of variable and size of each variable
#constructor allocates the size to object
#namespace is an area where u create and store object/variable. attributes r variables, behaviour r methods,functions.


""" --------------------------Instance,class,static methods -------------------------------------
class student:        #outer class
    school="Telusko"
    def __init__(self,m1,m2,m3):   #instance methods
        self.marks1= m1
        self.marks2 = m2
        self.marks3 = m3
        # we can create object of inner class(students_laptop) below  inside the outer class
        self.stu_lappi = self.students_laptop()

    def avg(self):      #instance methods
        return (self.marks1+ self.marks2+self.marks3)/3

    def show(self):
        print(self.m1)
        self.stu_lappi.show()

    def get_m1(self):   #getters/accessors
        return self.m1

    def set_m1(self,value):  #setters/mutators
        self.m1=value

    @classmethod     #class method
    def info(cls):
        return cls.school
    @staticmethod
    def getinfo():  #staic method
        print("get all info about school")

    class students_laptop:  #inner classs
        def __init__(self):
            self.brand="samsung"
            self.amount=60000
            self.graphics="amd"

        def show(self):
            print(self.brand,self.amount)


s1=student(48,38,73)
s2=student(58,88,43)
# print(s1.avg())
# print(student.info())   #class.method
# print(student.getinfo())   #staic method

s1.show()


#accessing the inner class from outside 
lap2=s1.stu_lappi
print(lap2.brand)



# we can create object of inner class outside the outer class provided we use outer class name
lap3=student.students_laptop()
print(lap3.amount)
"""


""" multilevel Inheritance
class A:
    def feature1(self):
        return ("its feature 1")

    def feature2(self):
        return ("its feature 2")


class B(A):   # multilevel inheritance
    def feature3(self):
        return ("its feature 3")

    def feature4(self):
        return ("its feature 4")

b=B()
print(b.feature3())
"""
""" multilevel inheritence with super and __init__
class Foo:
    def __init__(self):
        self.foo = 'foo'
        print("enter in foo")
class Boo:
    def __init__(self):
        self.Boo = 'Boo'
        print("enter in Boo")
class Bar:
    def __init__(self, bar,x,y):
        self.bar = bar
        self.x=x
        self.y=y
        print(x*y)
        print("enter in Bar")
    def add2(self):
        print(self.x+self.y)
# class FooBar(Foo, Bar):
#     def __init__(self,bar='bar'):
#         Foo.__init__(self)  # explicit calls without super
#         Bar.__init__(self,bar,10,3)
#         print("enter in FooBar")

class FooBar(Foo, Bar,Boo):
    def __init__(self,bar='bar'):
        super().__init__() # explicit calls without super
        super(Foo,self).__init__(bar,10,7)
        super(Bar, self).__init__()
        print("enter in FooBar")

obj2=FooBar()
obj2.add2()


class Foo:
    def __init__(self):
        self.foo = 'foo'
        print("enter in foo")
        super().__init__()
class Boo:
    def __init__(self):
        self.Boo = 'Boo'
        print("enter in Boo")
        super().__init__()
class Coo:
    def __init__(self):
        self.foo = 'foo'
        print("enter in Coo")
        super().__init__()


class combine(Foo,Boo,Coo):
    def __init__(self):
        super(combine, self).__init__()
        print("enter in combine")

combine_obj1=combine()
#----------with super in each class and parameters--------------
class First:
    def __init__(self,first,x,**kwargs):
        self.first = first
        self.x=x
        print("enter in 1st")
        super().__init__(**kwargs)
     def add2(self,y):
        self.y=y
        print(y+self.x)    
class Second:
    def __init__(self,second,**kwargs):
        self.second = second
        print("enter in 2nd")
        super().__init__(**kwargs)
class Third:
    def __init__(self,third,**kwargs):
        self.third = third
        print("enter in 3rd")
        super().__init__(**kwargs)

class Combined(First,Second,Third):
    def __init__(self,f,s,t,x):
        print("combined classes")
        super().__init__(first=f,second=s,third=t,x=x)
c=Combined("abc","xyz",4,10)
print(c.first)
print(c.third)
print(c.x)
c.add(50)
"""
#----------------------------------------------------------------

"""multiple inheritance
class A:
    def feature1(self):
        return ("its feature 1")

    def feature2(self):
        return ("its feature 2")


class B:   # multilevel inheritance
    def __init__(self):
        print("abc")
    def feature3(self):
        print ("its feature 3")

    def feature4(self):
        return ("its feature 4")

class C(B,A):
    def feature5(self):
        return ("its feature 5")
   
c=C()
print(c.feature1())
print(c.feature3())
"""
###################################################################
"""
# constructor inheritance
#if you create object of child class it will first try will find init of child class.if its not there in child,then checks in parent

class A:
    def feature1(self):
        print ("its feature 1-A")

    def feature2(self):
        return ("its feature 2-A")

class B(A):
    def __init__(self):  # init in child class
        print("BBBBB")
    def feature1(self):
        print ("its feature 3-B")

    def feature2(self):
        return ("its feature 4-B")
b=B()
b.feature1()
#o/p= BBBBBBB , its features 3-B
---------------------------------------------------------------------------
class A:     
    def __init__(self):  # init in parent class
        print("AAAAA")
    def feature1(self):
        print ("its feature 1-A")

    def feature2(self):
        return ("its feature 2-A")

class B(A):


    def feature1(self):
        print ("its feature 3-B")

    def feature2(self):
        return ("its feature 4-B")
b=B()
b.feature1()

#O/P---AAAAAA   ,its features 3-B

--------------------------------------

class A:
    def __init__(self):
        print("AAAAAAAA")
    def feature1(self):
        print ("its feature 1-A")

    def feature2(self):
        return ("its feature 2-A")

class B(A):
    def __init__(self):  
        # super().__init__()   # parent init is called first then child
        print("BBBBB")
    def feature1(self):
        print ("its feature 3-B")

    def feature2(self):
        return ("its feature 4-B")
b=B()

#O/P---    AAAAAAA, BBBBBB

------------------------------------------------
class A:
    def __init__(self):
        print("AAAAAAAA")
    def feature1(self):
        print ("its feature 1-A")

    def feature2(self):
        print ("its feature 2-A")

class B:
    def __init__(self):
        print("BBBBB")
    def feature3(self):
        print ("its feature 3-B")

    def feature4(self):
        return ("its feature 4-B")

class C(B,A):   # Method resolution order ( B is inherited first,then A as we defined (B,A)
    def __init__(self):
        super().__init__()
        print("CCCCCC")
    def feature1(self):
        print ("its feature 1-C")

    def feat(self):
        super().feature2()

c=C()
c.feat()
#O/P--- BBBBB,CCCCCC ,its features 2-A
"""


######-----------POLYMORPHISM(duck typing,method overloading,operator overloading,method overriding------------
class myeditor:
    def execute(self):
        print("compiling")
        print("running")

class laptop:
    def code(self,editor):
        editor.execute()
editor=myeditor()
ide=laptop()
ide.code(editor)

#--------------- operator overloading
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2 = m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2 = self.m2 + other.m2
        s3=student(m1,m2)
        return s3

s1=student(65,95)
s2=student(63,93)
s3=s1+s2
print(s3.m1)

#in python we dont have method overloading i.e method with same name different arguments.






#method overriding

class A:
    def __init__(self):  # init in parent class
        print("AAAAA")
    def feature1(self):
        print ("its feature 1-A")

    def feature2(self):
        return ("its feature 2-A")

class B(A):


    def feature1(self):
        print ("its feature 3-B")

    def feature2(self):
        return ("its feature 4-B")
b=B()
b.feature1()


# overriding is run time polymorphism , overloading is compiletime polymorphism














