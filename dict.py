dict = {"Name":"Aditya","Roll No":93,"Class":"SY-B"}
print(dict)

print(dict["Name"])
print(dict["Roll No"])
print(dict["Class"])

dict["Age"]=19
print(dict)

dict["Roll No"]=104
print(dict)

dict.pop("Class")
print(dict)

if "Name" in dict:
    print("It is present")
else:
    print("It is not present")

print(dict.keys())
print(dict.values())
print(dict.items())