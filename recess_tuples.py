#turples are ordered and immutable lists. they allow duplicate members
X = ("samsung", "iPhone", "techno", "redmi")
print(X[1])
print(X[-2])
#cant update iPhone to itel bse turples are immutable. also cant add new items directly
Y = ("Huawei",)
new_tuple = X + Y
print(new_tuple)
for phone in new_tuple:
    print(phone)
#del new_turple[0] cant directly delete an item from a turple so we first change the turple into a list
temp_list = list(new_tuple) #converts tuple into a list
print(temp_list)
del temp_list[0] #deletes the first item of the list
print(temp_list)
current_tuple = tuple(temp_list) #converts the list back to a turple 
print(current_tuple)

#new tuple of countries
countries = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
a, b, c, d, e = countries #unpacking a tuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(countries[1:4])

first_name = ("NALUYANGE")
last_name = (" KEVIN")
full_name = first_name + last_name
print(full_name)

colors = ("red", "blue", "green", "yellow")
multiplied_colors = colors * 3
print(multiplied_colors)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)