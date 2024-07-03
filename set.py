myset={"mango","cherry","cherry","banana"}
print(myset)
print(len(myset))
print(type(myset))
print("mango")
print("mango" in myset)
print("graps" not in myset)
#add
myset.add("apple")
print(myset)
thisset={"toamto","chili","onion","poatato"}
thisset.update(myset)
print(thisset)
#remove
myset.remove("banana")
print(myset)
myset.pop()
print(myset)
myset.clear()
print(myset)
del myset
print(myset)

#union
set1={"a","b","c",}
set2={1,2,3}
set3=set1.union(set2)
print(set3)
set4={"banana","naval","apple","mango"}
set5={"sabeeda","anil","hasib","nandhu"}
myset=set1.union(set3,set4,set5)
myset=set1|set2|set4|set5
print(myset)
#update
set4.update(set2)
print(set4)
#intersection(senter bagam)
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.intersection(set2)
set
set3=set1&set2
print(set3)

set1.intersection_update(set2)
print(set1)
#diffre

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1-set2
set1.difference(set2)

set1.difference_update(set2)
print(set1)
#cimatric diff
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.symmetric_difference(set2)
set1^set2
set1.symmetric_difference_update(set2)
print(set1)

x={"A","B","C"}
y={"F","E","D","C","B","A"}
z=x.issubset(y)
print(z)
x<=y

x={"apple","banana""cherry"} 
y={"google","microsoft","facebook"}
x.isdisjoint(y)


