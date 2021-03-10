"""
class Test(object):
    def __init__(self,num=1):
        self.num=num
        self.__numa=122    #double underscore of variable is protected and cant be accessed through object. it require geters

    def get(self):     #getters
        return self.__numa

    def set(self,num):
        self.__numa=num

    @property
    def methoda(self):
        print(" i m method A")

    @staticmethod
    def methodb():
        print(" i m static")


if __name__=="__main__":
    obj=Test()
    print(obj)
    print(obj.get())
    obj.methoda
    obj.methodb()

#--------------------------------------------------------------------------------------------------------------------------------


class person:
    def __init__(self, name):
        self.__name=name
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    def delname(self):
        print('delname() called')
        del self.__name
    # Set property to use get_name, set_name
    # and del_name methods
    name=property(getname, setname, delname)
p1=person()
p1.name="xy"

#------------------------------------------------------------ property decorator-----------

class House:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price

house=House(5000.0)
print(house.price) # calling getter
house.price=4000.0
print(house.price)  #calling setter
del house.price




#M2 method off creating class
class B:
    def __new__(cls, *args, **kwargs):
        return super(B,cls).__new__(cls, *args, **kwargs)
    def __init__(self,*args, **kwargs):
        super(B,self).__init__(*args, **kwargs)

#M3 method of creating class
class C:
    def __call__(cls, *args, **kwargs):
        return super(C,cls).__call__(*args, **kwargs)

#M4 method of creating class with metaclass. class is inherited
class D(type):
    def __call__(cls, *args, **kwargs):
        instance=super(D,cls).__call__(*args, **kwargs)
        return instance
    def __init__(cls,name,base,attr):
        super(D,cls).__init__(name,base,attr)


class E(metaclass=D):
    pass


# singelton design pattern (will let u create only one instance of the class(object))
class F(type):
    _instance={}
    # this is singelton design pattern
    def __call__(cls, *args, **kwargs):
        # if instance already exists then dont create
        if cls not in cls._instance:
            cls._instance[cls]=super(F,cls).__call__(*args, **kwargs)
            return cls._instance[cls]

class G(metaclass=F):
    def __init__(self):
        pass

obj=G()
print(obj)
obj1=G()   #it wont let u create 2nd object,gives None output.
print(obj1)



# Factory design pattern
class A:
    def __init__(self):
        pass
    def printa(self):
        print("A")

class B:
    def __init__(self):
        pass
    def printb(self):
        print("B")

def get(obj=""):
    objs=dict(a=A(),b=B())
    return objs[obj]
a=get('a')
a.printa()
b=get('b')
b.printb()



# ----------------------------------------Facade design pattern-------------------------------------
class SENSOR:
    def __init__(self):
        pass
    def sensorON(self):
        print("sensor On")
    def sensorOFF(self):
        print("sensor OFF")


class SMOKE:
    def __init__(self):
        pass

    def smokeON(self):
        print("smoke On")

    def smokeOFF(self):
        print("smoke OFF")

class LIGHTS:
    def __init__(self):
        pass

    def lightsON(self):
        print("light On")

    def lightsOFF(self):
        print("light OFF")

class Facade:
    def __init__(self):
        self._sensor=SENSOR()
        self._smoke=SMOKE()
        self._light=LIGHTS()
    def Emergency(self):
        self._sensor.sensorON()
        self._light.lightsON()
        self._smoke.smokeON()

    def NoEmergency(self):
        self._sensor.sensorOFF()
        self._smoke.smokeOFF()
        self._light.lightsOFF()

if __name__=="__main__":
    facade=Facade()
    sensor=30
    if sensor>60:
        facade.Emergency()
    else:
        facade.NoEmergency()
"""

# --------------------------------FACADE - sigelton design pattern-------------------------------------------------------
class SENSOR:
    def __init__(self):
        pass
    def sensorON(self):
        print("sensor On")
    def sensorOFF(self):
        print("sensor OFF")


class SMOKE:
    def __init__(self):
        pass

    def smokeON(self):
        print("smoke On")

    def smokeOFF(self):
        print("smoke OFF")

class LIGHTS:
    def __init__(self):
        pass

    def lightsON(self):
        print("light On")

    def lightsOFF(self):
        print("light OFF")

class Meta(type):
    _instance={}
    # this is singelton design pattern
    def __call__(cls, *args, **kwargs):
        # if instance already exists then dont create
        if cls not in cls._instance:
            cls._instance[cls]=super(Meta,cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class Facade(metaclass=Meta):
    def __init__(self):
        self._sensor=SENSOR()
        self._smoke=SMOKE()
        self._light=LIGHTS()
    def Emergency(self):
        self._sensor.sensorON()
        self._light.lightsON()
        self._smoke.smokeON()

    def NoEmergency(self):
        self._sensor.sensorOFF()
        self._smoke.smokeOFF()
        self._light.lightsOFF()

if __name__=="__main__":
    facade=Facade()
    sensor=30
    if sensor>60:
        facade.Emergency()
    else:
        facade.NoEmergency()






































