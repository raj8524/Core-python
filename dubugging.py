def add(x,y):
    sum=x+y
    return sum
if __name__=="__main__":
    x=input("num1: ")
    y = input("num2: ")
    z=add(x,y)
    print(z)

#from python terminal : python -m pdb dubugging.py
"""
n-next,c-continue,s-step intto,whatis- to get datatype of variable,where-to find to which line execution is
pdb> break 9(line number)
q-quit to come out of pdb

breakpoint-after setting brerakpopint to any line,execution will stop to that line.

"""
