mydict={"brand":"frord","model":"mustang","year":1964}
print(mydict)
type(mydict)
mydict.keys()
mydict.values()
mydict["model"]
mydict.get("model")
#dict
phonebook=dict({"name":"anil","country":"india","telephone":1234})
print(phonebook)
person=dict([("name","sachu"),("country","london"),("telephone",90485)])
print(person)
#marksheet
marksheet=dict({"name":["anil","sachu","ani"],"english":[55,25,45],"maths":[54,12,60]})
print(marksheet)
marksheet["english"]
marksheet["maths"]
phonebook["name"]="john"
print(phonebook)
phonebook["place"]="kerala"
print(phonebook)
phonebook.update({"place":"perinthalmanna"})
print(phonebook)
phonebook.update({"state":"kerala"}
print(phonebook)
phonebook.pop("state")
print(phonebook)
phonebook.popitem()
print(phonebook)
del phonebook["name"]
print(phonebook)
phonebook.clear()
print(phonebook)
del phonebook
print(phonebook)
len(marksheet)
print(mydict)
mydict.setdefault("colour","white")
print(mydict)
mydict2=mydict.copy()
print(mydict2)
dict3=dict(mydict)
print(dict3)
dict4=dict(mydict.items())
print(dict4)
#grp dict
jessa={'name':'jessa','state':'texas','city':'houston','marks':75}
emma={'name':'emma','state':'texas','city':'dallas','marks':60}
kelly={'name':'kelly','state':'texas','city':'austin','marks':85}
class_six={'student1':jessa,'student2':emma,'student3':kelly}
print("student 3 name:",class_six['student3']['name'])
print("student 3 marks:",class_six["student3"]['marks'])

#maximum,minimum
dict1={"c":45,"b":95,"a":35}
print(sorted(dict1.items()))
print(sorted(dict1.values()))
print(sorted(dict1))
print(max(dict1))
print(min(dict1))



