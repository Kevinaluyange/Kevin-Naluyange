Shoes = {
    "brand" : "Nick",
    "color" : "black",
    "size" : 40
}
print(Shoes["size"])
Shoes['brand'] = 'Adidas'
print(Shoes)
Shoes['type'] = 'sneakers'
print(Shoes)

#returning a list of keys and that of values
keys_list = list(Shoes.keys())
print(keys_list)
values_list = list(Shoes.values())
print(values_list)

#check if a certain key exists
if "size" in Shoes:
    print("Key exists")
else:
    print("Key doesnt exist")

#loop through the dictionary
for key, value in Shoes.items():
    print(key, ":", value)

#removing a key-value pair from the dictionary
del Shoes["color"]
print(Shoes)

#emptying a dictionary
Shoes.clear()
print(Shoes)

#a dictionary of my choice and a copy of it
Student = {
    "name" : "John",
    "age" : 24,
    "grade" : "A",
    "CGPA" : 4.9
}
student_copy = Student.copy()
print(student_copy)

#nested dictionary
myStudent = {
    "Student1" : {
        "name" : "Doe",
        "age" : 19,
        "course" : "BSSE"
    },
    "Student2" : {
        "name" : "Alice",
        "age" : 10,
        "course" : "BIST"
    }
}