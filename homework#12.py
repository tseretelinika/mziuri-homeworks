# # #1
# # while True:
# #     try:
# #         a = int(input("1st number:"))
# #         b = int(input("2nd number:"))
# #         c = a / b
# #         print(c)
# #     except ZeroDivisionError:
# #         print("you cant put number 0")
# #     except ValueError:
# #         print("you can only put numbers")
#
# # #2
# # def divide(a, b):
# #     try:
# #         return a / b
# #     except ZeroDivisionError:
# #         return "you can't divide by zero"
# #     except TypeError:
# #         return "you can only put numbers"
# #
# # try:
# #     x = float(input("First number: "))
# #     y = float(input("Second number: "))
# #     print(divide(x, y))
# # except ValueError:
# #     print("you can't put words")
#
# # #3
# # ran_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # try:
# #     print(ran_list[15])
# # except IndexError:
# #     print("Index out of range")
# #
# #4
# # try:
# #     with open("myresult.txt", "r") as f:
# #         content = f.read()
# # except FileNotFoundError:
# #     print("File not found")
#
# #5
# import math
# from logging import exception
#
# try:
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     c = float(input("Enter a third number: "))
#     if a == 0:
#         print("This is not quadratic equation")
#     else:
#         D = b*b - 4*a*c
#
#         if D > 0:
#             x1 = (-b + math.sqrt(D))/(2*a)
#             x2 = (-b - math.sqrt(D))/(2*a)
#             print("The x1 is", x1)
#             print("The x2 is", x2)
#
#         elif D == 0:
#             x = -b/(2*a)
#             print("The x is", x)
#         else:
#             print("no real root")
# except ValueError:
#     print("please enter a number")
#
# #6
# try:
#     a = 5
#     b = 3
#     c = 7
#     if a + b > c and a + c > b and b + c > a:
#         avarage = (a + b + c) / 3
#         print("The average is", avarage)
#     else:
#         raise ValueError("this is not triangle")
# except exception as m:
#     print(m)




