"""
class Employee:
    def __init__(self,first,last,x,y):
        self.first=first
        self.last=last
        self.x=x
        self.y=y
        self.z=x+y
        self.email=self.first+"."+self.last+'@gmail.com'
    def fullname(self):
        return f'{self.first} {self.last}'

emp_1=Employee('corey','schafer',8,9)
emp_1.first='jim'
emp_1.x=10
print(emp_1.first)
print(emp_1.email)  # its value remains corey schafer not jim schafer
print(emp_1.fullname())
print(emp_1.z)


class Employee:
    def __init__(self,first,last,x,y):
        self.first=first
        self.last=last
        self.x=x
        self.y=y
        self.z=x+y
    def fullname(self):
        return f'{self.first} {self.last}'
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

emp_1=Employee('corey','schafer',8,9)
emp_1.first='jim'
emp_1.x=10
print(emp_1.first)
print(emp_1.email())  #its now got changed to jim schafer
print(emp_1.fullname())
print(emp_1.z)

"""
class Employee:
    def __init__(self,first,last,x,y):
        self.first=first
        self.last=last
        self.x=x
        self.y=y
        self.z=x+y

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
    @property
    def fullname(self):     #its like getter
        return f'{self.first} {self.last}'
    @fullname.setter
    def fullname(self,name):   #setter
        first,last=name.split(" ")
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print('Delete name ...')
        self.first=None
        self.last=None
emp_1=Employee('corey','schafer',8,9)
emp_1.first='jim'
print(emp_1.email)
emp_1.fullname="raj kumar"
emp_1.x=10
print(emp_1.first)
print(emp_1.email)  #its now got changed to jim schafer. email method canbe accessed as now attribute.
print(emp_1.fullname)
del emp_1.fullname
print(emp_1.fullname)
# print(emp_1.z)





































