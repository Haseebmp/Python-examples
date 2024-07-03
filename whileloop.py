# Calculate the sum of natural numbers until the sum becomes greater than 100.
sum=0
i=1
while sum<=100:
    sum=sum+i
    i=i+1
    print(sum)

#for
sum=0
for num in range(0,101):
    sum=sum+num
    print(sum)
    if sum >100:
        break
              
#Execute loop until list becomes empty.
num1=[1,2,3,4,5,6,7,8,9,10]
while len(num1)>0:
    num1.pop()
print()                        

