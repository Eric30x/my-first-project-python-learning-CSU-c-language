# 定义一个类Son,继承自上节课作业所定义的父类Person类
#  1.导入上节课作业的Person类进行继承使用
#  2.Son类里定义一个连续移动方法:
#           只要体力值允许,一直继承调用父类Person类的移动方法(move),直到体力值不足
#  3.Son类里定义一个连续攻击方法:
#           只要生命值允许,一直继承调用父类Person类的攻击方法(attack),直到生命值不足
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
class son(Person):
    def __init__(self, name, hp, body):
        self.name = name
        self.hp = hp
        self.body = body
    def _move(self):
        if self.body >= 10:
            self.body -= 10

        super().move()
    def attack(self):
        super().attack()
man=son("xiaomin",20,50)
man.move()
man.attack()


























