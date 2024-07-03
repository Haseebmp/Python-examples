car1=["swift","alto","fronx","benz"]
num1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in num1:
    print(i)
for j in range(0,len(num1)):
    print(num1[j])

#while
num1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num2=0
while num2 <len(num1):
    print(num1[num2])
    num2=num2+1

#for(pattern)
star=["*","**","***","****","*****","******"] 
for k in star:
    print(k)  
 #c     
for row in range(0,6):
    for col in range(0,row):
      print("*",end="")
    print("")  

for row in range(0,6):
    for col in range(0,row):
        print(col,end="")
    print("")

#pyramid star method1 
"""
    *
   ***
  *****
 *******
********* """
n=5
for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end="")
    for star in range(2*i-1)   :
        print("*",end="") 
    print("")
#method 2
n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))

""""
*********
 *******
  *****
   ***
    *   """
n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))


"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *  """

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))

""""
*
**
***
****
*****
****
***
**
*   """
for row in range(0,6):
    for col in range(0,row):
      print("*",end="")
    print("")  
for row in range(row,0,-1):
    for col in range(0,row):
      print("*",end="")
    print("")  

""""
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    * """
for row in range(0,6):
    for col in range(0,row):
      for space in range(6-row):
          print("*",end="")
    print("")  

 #
for a in range(1500,2701):
    if a % 7==0 or a % 5==0:
        print(a)
    
#0 to 6 except 3and 6
for num in range(0,7):
    if num==3 or num==6:
        continue
    print(num)

for num in range(0,7):
    if num==3:
        break
    print(num)

a=int(input('enter a number'))
for num1 in range(0,101):
    if num1==a+1:
        break
    print(num1)
#
s=input("enter a string contains characters and numbers")
for s1 in range(len(s)):
    print(s[s1])


s=input("enter a string contains characters and numbers")
characters=0
digits=0
for s1 in s:
    if s1.isalpha():
      characters+=1
    elif s1.isdigit(): 
      digits+=1
    else:
        pass
  
print(characters)
print(digits)   

#
s=input("enter a string contains characters and numbers")
characters=0
digits=0
others=0
for s1 in s:
    if s1.isalpha():
      characters+=1
    elif s1.isdigit(): 
      digits+=1
    else:
        others+=1
print(characters)
print(digits) 
print(others)  
    