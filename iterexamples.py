#iter function
list1=[1,2,3,4,5,6,7,8,9,10]
list2=iter(list1)
next(list2)

#filiter function
ages=[12,4,7,15,18,23,22,20,19]

for b in ages:
    if b >= 18:
       print(b)
def cl (d):
    if d <18:
        return True
    else:
        return False
list(filter(cl,ages) )          

#numpy
import numpy as np
list1=[1,2,3,4,5,6]
ar1=np.array(list1)
type(ar1)
ar1
list2=[22,"haseeb",25,47,96,True,False]
ar2=np.array(list2)
ar2
ar1.sum()
ar1.min()
ar1.max()
ar1.mean()
ar1.shape

#o-D arrays Dimensions
list6=[42]
ar4=np.array(list6)
ar4
ar4.shape
#1-D arrays Dimensions
list8=[1,2,5,3,69,14]
ar8=np.array(list8)
ar1
ar1.shape
#2-D arrays Dimensions
list7=[[1,5,78,96,54],[1,5,2,65,48,]]
ar5=np.array(list7)
ar5
ar5.shape
#3-D arrays Dimensions
list9=[[1,5,78,96,54],[1,5,2,65,48,],[1,2,3,78,95.25]]
ar9=np.array(list9)
ar9
ar9.shape


