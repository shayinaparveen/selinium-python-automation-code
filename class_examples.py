# v = "almas"
# print(v)


# class ex:
#     v1 = str(input("Enter the v1 value: "))
#
#
# print(ex().v1)
# print(ex.v1)

# class ex:
#     v1 = str(input("Enter the v1 value: "))
#
#     #    v2 = str(input("Enter the v2 value: "))
#
#     def f1(self):
#         print("Method inside function")
#         print(ex().v1)
#         print(self.v1)
#
#     # def f2(self):
#     #     print("Method inside function")
#     #     print(ex.v2)
#     #     print(self.v2)
#
#
# print(ex().v1)
# print(ex().f1())
# # print(ex().f2())
#
# e1 = ex()
# print(e1.v1)
# print(e1.f1())


# class square:
#     def __init__(self, length, width):
#         print("Start")
#         self.l = length
#         self.w = width
#         print("Stop")
#
#     def area(self):
#         a = self.w * self.l
#         print("Area = ", a)
#
#
# s = square(10, 20)
# print(s.area())
#
#
# class cube(square):
#     def __init__(self, height):
#         self.h = height
#
#     def rect(self):
#         c = self.l + self.w + self.h
#         print("cube value", c)
#
#
# c = cube(2, 3)
# # print(c.area())
# # print(c.rect())

# class example:
#     variable = 125
#
#
# c = example.variable
# print(c)
# d = example().variable
# print(d)

# class example:
#     variable = 125
#
#     def b(self):
#         print("This is the example class")
#         print(example.variable)
#         print(self.variable)
#
#
# e1 = example()
# print(e1.variable)
# print(e1.b())

# class square:
#     def __init__(self, length, width):
#         print("Start")
#         self.l = length
#         self.w = width
#         print("Stop")
#
#     def area(self):
#         a = self.w * self.l
#         print("Area:", a)
#
#
# # s = square(20, 30)
# # print(s.area())
#
#
# class box(square):
#     def box1(self):
#         print("child Class")
#
#
# b = box(2, 3)
# print(b.box1())
# print(b.area())

# class emp_personal_details:
#     name = "Almas"
#     Address = "Perumbakkam"
#     Phone = "9790262886"
#
#     def emp(self):
#         print(self.name)
#         print(self.Address)
#         print(self.Phone)
#
#
# class emp_office_details(emp_personal_details):
#     name = "Almas"
#     emp_id = 9790262886
#
#     def emp_off(self):
#         print(self.name)
#         print(self.emp_id)
#
#
# e = emp_office_details()
# print(e.emp())
# print(e.emp_off())


class addition:
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))

    def sum(self):
        z = self.x + self.y
        print("Addition of 2 numbers:", z)


class s1(addition):
    # v = addition
    # v.x = int(input("Enter the value of x: "))
    # v.y = int(input("Enter the value of y: "))

    def sub(self):
        z = self.x - self.y
        print("Substration of 2 numbers:", z)


class multiplication(s1, addition):
    def mult(self):
        z = self.x * self.y
        print("Multiplication of 2 numbers:", z)


class division(multiplication, s1, addition):
    def div(self):
        z = self.x / self.y
        print("Division of 2 numbers:", z)


d = division()
print(d.sum())
print(d.sub())
print(d.mult())
print(d.div())

