beverages = set(["fanta", "pepsi", "coke"])
print(beverages)
beverages.update(["krest", "novida"])
print(beverages)
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Yes, microwave available in set")
else:
    print("No microwave in set")
    
mySet.remove("kettle")
print(mySet)
for item in mySet:
    print(item)

#new dict
myElements = {"book", "pen", "paper", "ruler"}
my_items = ["rubber", "duster"]
new_items = set(["rubber", "duster"])
combined = myElements.union(new_items)
print(combined)

age = {25}
name = {"NALUYANGE KEVIN"}
details = age.union(name)
print(details)