#Variables
# x = 24
# y = "Arkiee"
# print(x)
# print(y)

# a = 4       # a is of type int
# a = "Arkiee" # a is now of type str
# print(a)

# #Casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# print(type(x)) #get the type of x
# print(type(y)) #get the type of y
# print(type(z)) #get the type of z

# #multiple variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

#Global and Local Variables
x = "awesome" #global variable

def myfunc():
  x = "fantastic" #local variable
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x #Global Keyword
  x = "fantastic"

myfunc()

print("Python is " + x)

#Casting
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'