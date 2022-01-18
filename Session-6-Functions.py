# def func1():
#     print ("code under function func1 is printed")
# func1()
# func1()
#
# def func2(val=3):
#     print("code under function func2 is printed")
#     print(val + val)
#     print("***********************")
#
#
# func2(val=5)


# func2(5)
# func2(val = 20)
#
# # scope #
#
# def my_func():
# 	x = 10
# 	print("Value inside function:",x)
# x = 20
# my_func()
# print("Value outside function:",x)

# # when return is encountered, it comes out of the function
# def add_numbers(x,y):
#    sum = x + y
#    return sum # returns sum
#    # #return  # returns None
#    # #if no 'return', None will be returned
#
# # num1 = 5
# # num2 = 6
#
# v = add_numbers(2,5)
# print ("value of v", v)


# when return is encountered, it comes out of the function

# def f1():
#     print ('hi')
#     return
#     print ('hussain')
# f1()


# def func2(val = 5):
#     print ("code under function func2 is printed")
#     print ( val + val)
# func2() # if we pass value, function will use it, else it uses default values
# func2(10)
#
# #def func3(val = 5, y): #SyntaxError: non-default argument follows default argument
# def func3(x,y = 5):
#     print ( "value of x + y = ", x + y)
#
# func3(2)
# func3(2,10)
# # When we call a function with some values, these values get assigned to the arguments according to their position
#
# def greet(name, msg="Good morning!"):
#     print("Hello", name + ', ' + msg)
#

# greet("Kate")
# greet("Bruce", "How do you do?")
#
# #Python allows functions to be called using keyword arguments.
# # When we call functions in this way, the order (position) of the arguments can be changed
# greet(msg = "How do you do?",name = "Bruce")
# greet(name="Bruce","How do you do?") #SyntaxError: non-keyword arg after keyword arg
#
# # Arbitrary Arguments ( when we are not sure how many elements to pass , use * )
# def greet(*names):
#     for name in names:
#         print("Hello", name)
# greet("Monica", "Luke", "Steve", "John")  #These arguments get wrapped up into a tuple before being passed into the function

# def greet(**dict1):
#     print (dict1)
# greet(a=1, b=2)
#
# def greet(*names):
#     print ('hi')
# greet()  # passing args and kwargs are optional
#
# def greet(a, *args, **kargs):
#     print("a is",a)
# greet(1)
#
# def greet(*args, a):
#     print (a)
# greet(1,2,3,a=4)
# #greet ( 1,2,3,4) # incorrect

def greet(a, b, c):
    print(a, b, c)


tuple1 = (1, 2, 3)
d1 = {"a": 1, "b": 2, "c": 3}
greet(*tuple1)
greet(**d1)


#


# lambda
# Program to show the use of lambda functions
# double = lambda x: x * 2
#
# print(double(5))

# variable x is defined outside of function, We can read these values from inside the function
# def my_func():
#     print("Value inside function:",x)
#
#
# x = 20
# my_func()
# print("Value outside function:",x)

# variable x inside the function is different (local to the function) from the one outside.
# Although they have the same names, they are two different variables with different scopes.
def my_func():
    # global x
    x = 10
    print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)

# we cant modify x inside function foo, until we declare it as global
# x = 3
# def foo():
#     x = x * 2  #UnboundLocalError: local variable 'x' referenced before assignment
#     print(x)
#
# foo()


# use the global keyword if you want to make a change to a global variable inside a function.
# x = 3
# def foo():
#     global x # if we modify global variable, the value reflects outside of the function as well
#     x = x * 2  #UnboundLocalError: local variable 'x' referenced before assignment
#     print(x) #6
#
# foo()
# print(x) #6

#########
# NameError: name 'y' is not defined
# def foo():
#     #global y
#     y = 1 # cannot use local variable , outside of the function . to make it work, delare it as 'global' like above line
# foo()
# print(y) # NameError: name 'y' is not defined


# Global variable and Local variable with same name
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available in the local scope (inside the function):
# x = 5
#
# def foo():
#     x = 10
#     print("local x:", x) # 10
# foo()
# print("global x:", x) # 5

# Global Variables Across Python Modules  (like params)
# https://www.programiz.com/python-programming/global-keyword

# Function Inside Function
# The local variable can be accessed from a function within the function:

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()
#
# myfunc()

# def f1():
#     global x
#     x = 10
#     print("value of x inside function f1", x)
#
#
# f1()
# print("value of x outside function f1", x)
