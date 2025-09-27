'''print("Hello, World!")
#strings
food = "rice"
print(f"I like {food}")
#integers
age = 21
print(f"I am {age} years old")
#floats
height = 5.11
print(f"My height is {height} feet ")
#booleans
man = True
print(f"Are you a man? {man}")
if man:
    print("You are a man")
else:
    print("You are not a man")
#multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(f"Fruits: {x}, {y}, {z}")
#typecasting
name = "aayush"
gpa = 9.8
age = 21
is_graduated = False
gpa = str(gpa)
print(gpa)
print(type(gpa))
'''
'''#user input
name = input("Enter your name: ")
print(f"Hello, {name}!")
age = int(input("Enter your age: "))
print(f"You are {age} years old")
height = float(input("Enter your height in feet: "))
print(f"You are {height} feet tall")'''
'''#exercise 1 area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area} square units")
'''
'''#exercise 2 shoping cart
item = input("Enter the item name ")
quantity = int(input("Enter the number of item "))
price = float(input("Enter the price of the item "))
total = (quantity) * (price)
print(f"  {quantity} {item} at price {price} is {total} ")'''
'''egg = 5
egg **= 3 #power
print(egg)'''
'''#maths functions
x =3.94
y = 7
z= 11
#result = round(x) #rounds to nearest integer
#result = abs(y) #absolute value - how much far from 0
#result = pow(y, 2) #y to the power of 2
#result = max(x, y, z) #maximum value 
#result = min(x, y, z) #minimum value
print(result)'''
'''import math
print(math.inf<100) # these 2 function can use for compaier
print(math.nan !=1) '''
'''#exercise math
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print (f"the radius of the circle is {radius}")
print(f"Circumference is {round(circumference,3)}")
print(f"Area is {round(area,3)}")'''
'''# hypo
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c= math.sqrt(a**2 + b**2)
print(f"The length of the hypotenuse is {round(c,2)}")'''
'''#hypotenuse
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c= math.hypot(a, b)
print(f"The length of the hypotenuse is {round(c,2)}")'''
'''#if 
age = int(input("Enter your age: "))
if age >= 18:
    print("you can vote ")
elif age == 17:
    print("you can pre-register to vote")
else:
    print("you cannot vote")'''
'''responce = input("would you like to download the file? (y/n)")
if responce.lower()=="y":
    print("downloading...")
else:
    print("exiting...   ")'''
'''#boolean if
available = False
if available:
    print("item is available")
else:
    print("item is not available")'''
