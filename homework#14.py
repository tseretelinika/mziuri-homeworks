# #1
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def display_balance(self):
#         if self.balance >= 2500:
#             print("you can only have $2500")
#         else:
#             print(self.balance)
#
# balance1 = BankAccount("John", 345)
# balance1.deposit(400)
# balance1.withdraw(100)
# balance1.display_balance()

#2
import math
class Shape:
    def __init__(self):
        print("i am a shape")

class Polygon(Shape):
    def __init__(self, *sides):
        super().__init__()
        self.sides = sides

class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return "aseti samkutxedi ar arsebobs"

        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

        return area
