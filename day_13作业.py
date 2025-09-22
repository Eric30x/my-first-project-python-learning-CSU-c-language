# 定义1个狗类:
# 1.定义4个实例属性
#    品种(style),年龄(age),颜色(color),饥饿程度(hunger)默认值为'很饿'
# 2.定义4个实例方法:
#                    1.打印当前狗对象的品种( get_style() )
#                    2.打印当前狗对象的年龄( get_age()  )
#                    3.打印当前狗对象的颜色( get_color() )
#                    4.打印当前狗对象的饥饿程度( get_hunger() )

# 3.实例化一条'拉布拉多' 2岁 黄色 不饿 的狗,分别调用所有实例方法
# 4.实例化一条'泰迪' 7岁 咖啡色 很饱 的狗,分别调用所有实例方法
class 狗:
    def __init__(self,style,age,color,hunger='很饿'):
        self.style=style
        self.age=age
        self.color=color
        self.hunger='很饿'
    def ideas(self):
        print(f"当前狗的品种{self.style}，年龄{self.age},颜色{self.color},饥饿程度{self.hunger}")
拉布拉多=狗('拉布拉多',2,'黄色','不饿')
泰迪=狗('泰迪',7,'咖啡色','很饱')
拉布拉多.ideas()
泰迪.ideas()









