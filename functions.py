sum=0
for num in range(0,101):
    sum=sum+num
    print(sum)
    if sum >100:
        break

def numbers():
    sum=0
    i=1
    while sum<=100:
      sum=sum+i
      i=i+1
      print(sum)
numbers()

def edit (p,u):
    sum=0
    for num in range(p,u):
        sum=sum+num
        print(sum)
        if sum >1000:
            break
edit(0,1500)  

def hasiib():
    a=int(input("staring"))
    list1=[]
    sum=0
    i=1
    while sum<=a:
            sum=sum+i
            i=i+1
            list1.append(sum)
    print(sum)           
hasiib()


def messi():
    a=int(input("starting point"))
    sum=0
    i=1
    list1=[]
    while sum<=a:
        sum=sum+i
        i=i+1
        list1.append(sum)
        return list1
messi()


def neymar(p,u):
        sum=0
        list1=[]
        for num in range(p,u):
            sum=sum+num
            print(sum)
            list1.append(sum)
            return list1
neymar(200,800) 
a=neymar(20,80)     

def bike (k):
 list3=[]
 for num in k: 
     list3.append(num) 
 return list3 
bike()
c=[1,2,3,4,5,6,7,8,9]
bike(c)


#default def

def sum1(a=78,b=0):
    c=a+b
    return c
sum1(b=34)
print(12,end="")

#default arugement value
def code1(a=13,b=0):
    z=a*b
    return z
code1(b=45)
s=code1(b=49)
s

def code (*hasiib):
    v=sum(hasiib)
    return v
code(10,2,78,25,36,456321456)
u=code(2,5) 
u

#
import operator
def mul2(*args):
    b=1
    for a in args:
        b=operator.mod(b,a)
    return b
mul2(10,10000)

#
def fun (**kwargs):
    for keys,values in kwargs.items():
        print("%s=%s"%(keys,values))
fun(Name="HASEEB",Course="PYTHON",Duration="1YEAR")      


 
  

           
        
                
            

 

