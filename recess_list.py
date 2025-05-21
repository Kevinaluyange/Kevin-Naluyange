#Lists are mutable
names_list = ["Kevin", "Cate", "Frank", "Musa", "Ken"]
print(names_list[1])

names_list[0] = "Ben"
names_list.append("Roger")
names_list.insert(2, "Bathel")
print(names_list)
del names_list[3]
print(names_list)
print(names_list[-1])

#new list
my_items = ["banana", 7, "Pea", 122, 45, "orange", "strawberry"]
print(my_items[2:5])

#list of countries
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "USA"]
copied_list = list(countries)
print(copied_list)
for country in countries:
    print(country)

#list of animal names
animal_names = ["snake", "zebra", "lion", "tiger", "antelope", "dog", "cow"]
print(sorted(animal_names))
animal_names.sort(reverse=True)
print(animal_names)
newlist = [animal for animal in animal_names if "a" in animal] #uses list compresion
print(newlist)
'''
for animal in animal_names:
    if "a" in animal:
        newlist.append(animal)
print(newlist)
'''

first_name = ["NALUYANGE"]
last_name = ["KEVIN"]
full_name = first_name + last_name
print(full_name)
'''
first_name.extend(last_name)
print(first_name)
'''