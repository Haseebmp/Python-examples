hasiib=[12,52,14,85,96,35]
def haseeb(b):
    return b%3
list(map(haseeb,hasiib))

#def add
def add(n):
    return n**n
numbers=(2,5,3,69,4)
answer=map(add,numbers)  
print(list(answer))  

from functools import reduce
def hasiib (h,b):
    return h-b
reduce(hasiib,numbers)