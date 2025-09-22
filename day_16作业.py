# 定义一个人类(Person)
# 具备:
#     1.姓名(name)
#     2.生命值(hp)
#     3.体力(body)
# 1.定义一个移动一次消耗10体力:move() # 需要判断体力值是否足够
# 2.定义一个攻击一次消耗5生命值:attack() # 需要判断生命值是否足够
# 3.每次打印这个对象,都能够显示对象的姓名和现在的生命值(hp)和体力(body)数据
# 4.删除这个对象时,会自动打印f'{name}已被删除'
# 5.调用这个对象不存在的属性时,会默认返回f'{属性名(变量)}不存在'
class Person:
    def __init__(self, name, hp, body):
        self.name = name
        self.hp = hp
        self.body = body

    def move(self):
        if self.body >= 10:
            self.body -= 10
            print(f"{self.name}移动了一次，消耗10体力")
        else:
            print(f"{self.name}体力不足，无法移动")

    def attack(self):
        if self.hp >= 5:
            self.hp -= 5
            print(f"{self.name}攻击了一次，消耗5生命值")
        else:
            print(f"{self.name}生命值不足，无法攻击")

    def __str__(self):
        return f"姓名: {self.name}, 生命值: {self.hp}, 体力: {self.body}"

    def __del__(self):
        print(f"{self.name}已被删除")

    def __getattr__(self, attr):
        return f"{attr}不存在"




