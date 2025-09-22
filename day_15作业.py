# 封装一个银行卡类:Card
# 1.Card类中有实例属性:
#           用户名:name
#           年龄:age
#           密码为私有属性:__password,
#           均可以从实例化对象过程中传入
# 2.定义一个实例方法get_user(),可以获取这并且打印用户信息(name和age)
# 3.定义一个修改密码的私有方法,__set_password()
# 4.定义一个实例方法,可以调用修改私有属性的方法,函数名称为:setpassword(),
#   如果检测到该方法传入的用户名称正确,则修改, 否则,提示'用户名称错误'
# class Card:
#     def __init__(self, name, age,password):
#         self.name = name
#         self.age = age
#         self.__password = password
#     def get_user(self):
#         print(self.name)
#         print(self.age)
#     def __set_password(self, password):
#         self__password={f'你将密码修改为:{password}'}
#         print(self__password)
#     def setpassword(name,age):
#         age=int(age)
#         if isinstance(name,str):
#             print(f'你将用户名修改为：{name}')
#         else:
#             print('用户名称错误')


# class Card:
#     def __init__(self, name, age, password):
#         self.name = name
#         self.age = age
#         self.__password = password
#
#     def get_user(self):
#         print(self.name)
#         print(self.age)
#
#     def __set_password(self, password):
#         self.__password = password
#         print(f'你将密码修改为: {self.__password}')
#
#     def setpassword(self, new_password):
#         if isinstance(self.name, str):
#             self.__set_password(new_password)
#         else:
#             print('用户名称错误')
class Card:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.__password = password
    def get_user(self):
        print(f"用户名: {self.name}")
        print(f"年龄: {self.age}")
    def __set_password(self, password):
        self.__password = password
        print(f'你将密码修改为: {self.__password}')
    def setpassword(self, input_name, new_password):
        if input_name == self.name:
            self.__set_password(new_password)
        else:
            print('用户名称错误')
my_card=Card('张三',25,12345)
my_card.get_user()






