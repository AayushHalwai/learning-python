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
'''#logical operators
day = "sunny"
temp = 30
if day == "sunny" and temp <20:
    print("it is a nice day")
elif day == "sunny" or temp == 30:
        print("it is a sunny day or temp is 30")
else :
        print("it is not a sunny day")
#not operator
if not day == "sunny":
    print("it is not a sunny day")'''
'''#conditional expressions
age = 10
#print("you can vote" if age>= 18 else "you cannot vote")
print("even" if age %2==0 else "odd")
'''
'''#validate user input
username = input("Enter your name: ")
if len(username)>12:
    print("username is too long then 12 characters")
elif  not username.find(" ") == -1:
    print("username cannot contain spaces")
elif not username.isalpha():
    print("username can only contain letters")
else:
    print(f"hello {username}")'''
'''#string indexing
credit_card = "1234-5678-9876-5432"
print(credit_card[1:10:2]) #start:end:step
print(credit_card[-4:]) #last 4 digits
print(credit_card[::2]) #every second digit'''
'''#format specifiers
cash1 = 10000.89833
cash2 = -30020.89989
print(f"${cash1:+,.2f}")
print(f"${cash2:+,.1f}")
print(f"${(cash2):^20.2f}")'''
#while loop
'''name = input("Enter your name: ")
while name == "":
    print("name not entered")
    name = input("enter your name: ") #untill user enter name the while loop will keep running

print(f"hello, {name}!")'''

'''num = int(input("enter num 1-10: "))

while num <1 or num >10:
    print("invalid")
    num = int(input("enter num 1-10: "))
print(f"you entered {num}")'''
'''#for loop
for x in range (1,11,2):
    print(x)


for x in reversed(range (1,11,2)):
    print(x)
print("/n")'''

'''for x in range (1,20):
    if x == 10:
        break
    else:
        print(x)'''
'''num = '12345679'
for x in num:
    print(x)'''