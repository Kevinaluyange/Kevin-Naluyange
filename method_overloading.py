class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):   #overloaded method which gets executed
        return a + b + c
    
my_calc = Calculator()
#print(my_calc.add(2, 4))
print(my_calc.add(5, 2, 3))