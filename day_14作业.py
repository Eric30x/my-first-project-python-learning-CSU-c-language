# 1.创建一个 长方形 Rectangle 类，具有计算长方形面积和周长的方法(return)
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         area = self.width * self.height
#         return area
#     def perimeter(self):
#         perimeter = self.perimeter
#         return perimeter
# a=Rectangle(4,5)
# print(a.area())



# 2.创建一个 银行账户 BankAccount 类，具有存款和取款的方法，并能够查询账户余额。
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance=self.balance+amount
#         print(f"存入{amount}元，当前余额：{self.balance}元")
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("余额不足！")
#         else:
#             self.balance -= amount
#             print(f"取出{amount}元，当前余额：{self.balance}元")
