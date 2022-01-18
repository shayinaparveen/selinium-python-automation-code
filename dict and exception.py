# # dict_1 = {1: 'Almas' , 2: 'Mohamed', 3: 'Shayina', 4: 'Parveen', 5:'Asfara', 6:'Alfarisha'}
# # print(dict_1)
# #
# # print(dict_1[4])
# #
# # # dict_1.clear()
# # # print(dict_1)
# # #
# # # del dict_1
# # # print(dict_1)
# #
# # dict_2 = dict_1.copy()
# # print(dict_2)
# #
# # dict_1 = {1: 'Almas' , 2: 'Mohamed', 3: 'Shayina', 4: 'Parveen', 5:'Asfara', 6:'Alfarisha'}
# # keys = dict_1.keys()
# # print(list(keys))
# # values = dict_1.values()
# # print(list(values))
#
#
# # d1 = {1: 'one' , 2:'two'}
# # d = {2: 'three'}
# # d1.update(d)
# # print(d1)
#
# # val = input("Enter your value: ")
# # if val == 10:
# #     try:
# #         print('val is',val)
# #     except Exception:
# #         print("Exception Occured, x is not found")
# # else:
# #     y= 20
# #     print(y)
#
# # x = 10
# # print ('x is',x)
# # y = 10
# # print ('y is', y)
# # try:
# #     print ('x is',x)
# #
# # except Exception:
# #     print ( "exception occured, x is not found")
# # finally:
# #     print("x is found and printed")
# #     y= 20
# #     print(y)
#
#
# # X = 10
# # try:
# #     print("X Value is",X)
# # except Exception ("Value of x is not found")
# # else:
# # y=10
# # print("Y value is ", y)
#
#
# # x1 = 10
# # try:
# #     print ('x is',x)
# #
# # except Exception:
# #     print ( "exception occured, x is not found")
# # finally:
# #     print("X is found and printed")
# #     y = 10
# #     print('Y value is', y)
#
#
# # val = int(input("Enter your value: "))
# # if val >= 10:
# #     raise Exception ("x value is not greater than 10")
# #
# #
# # x = 'hello1'
# # assert x == 'hello', "x should be hello"
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "dummy": "dummy1"
# }
#
# thisdict.pop("year")
# print(thisdict)
#
# print(thisdict.get("brand"))
# print(thisdict["brand"])
#
# thisdict["brand"] = 'newFord'
# print(thisdict)
# print(thisdict['model'])
# keys = thisdict.keys()
# print(keys)
# if thisdict["dummy"] == 'dummy1':
# try:
#     print("Value found")
# except Exception ("Dummy" is not found in thisdict):
# else:
#         print("Exception is found and not found")
#
#
# X = 10
# try:
#     print("X Value is",X)
# except ("Value of x is not found")


# thisdict.pop("year")
# print(thisdict)
#
# print(thisdict.get("brand"))
# print(thisdict["brand"])
#
# thisdict["brand"] = 'newFord'
# print(thisdict)
# print(thisdict['model'])
# keys = thisdict.keys()
# print(keys)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "dummy" : "dummy1"
#
# }
# if thisdict.values() == "dummy1":
#     try:
#        print("Value found")
#     except:
#        print("Dummy not found")
# # else:
# #         print("Exception is found and not found")


# Create a function to find multiply of three values.
#
# define function in a .py file, and call the function in other .py file.


# def multiplication(x,y,z):
#     a =  x * y * z
#     print(a)
#     return a
#
# x = 10
# y = 20
# z = 30
#
# multiplication(x,y,z)

# def f1(b, a=10):
#     c = a + b
#     return c
#
#
# v = f1(20, 20)
# print(v)

def add(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


def mul(a, b):
    c = a * b
    return c


def div(a, b):
    c = a / b
    return c


x = int(input("Enter the Value of X:"))
y = int(input("Enter the Value of y:"))

print("Addition of 2 numbers", add(x, y))
print("Substraction of 2 numbers", sub(x, y))
print("Mutliplication of 2 numbers", mul(x, y))
print("Division of 2 numbers", div(x, y))
