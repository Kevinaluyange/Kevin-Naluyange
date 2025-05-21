

#x = (1 == True)
#y = (1 == False)

#a = True + 4
#b = False + 10

#print("the value of a is", x)

#print("the value of b is", y)

#print("a", a)
#print("b", b)

#print("Our first programs in Python")

#a = 100
#b = 200

#c = a + b

#print("the total value C is", c)

##how to use the format method to add variables to a string
#Age = 6
#Txt = "i am {} years old"
#print(Txt.format(Age))
#Txt2 = "my name is {}. i am {} years old"
#print(Txt2.format( "Moses", Age))


#X = 'Python'
#Y = 'is'
#Z = 'interesting'
#print(X + " " + Y + " " + Z)
#print(X,Y,Z)

#X = 5
#Y = "JOHN"
#print(X,Y)



class Restaurant:
  def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

  def describe_restaurant(self): 
       print(self.restaurant_name + " has nice interior.")
  def open_restaurant(self):
        print(self.restaurant_name + " is OPEN")
restaurant = Restaurant("Cafe Javas", 9)
print("My restaurant's name is " + restaurant.restaurant_name.upper())
print("My restaurant's cuisine falls under category " + str(restaurant.cuisine_type))
restaurant.describe_restaurant()
restaurant.open_restaurant()