# 1.将列表 ['1','2','1','3','4','4','5','5','6','2','3','6'] 去重
# (最终结果保持数据类型不变,即还是列表)
# (提示:使用for循环,可引入一个空列表)
# a=['1','2','1','3','4','4','5','5','6','2','3','6']
# b=set(a)
# b=list(b)
# print(b)




# 2.将[1,2,[3,4]]中的每个整数按照顺序
# 添加到空列表 list_01 中, 形成[1,2,3,4]列表
# (2种方法:索引取值再添加 和 循环,任选其1即可)
# a=[1,2,[3,4]]
# list_01=[]
# for i in a:
#     if type(i)==list:
#         list_01.extend(i)
#     else:
#         list_01.append(i)
# print(list_01)



# 饼干盒们 = [ ["巧克力饼干", "草莓饼干"], ["奶油饼干"], ["动物饼干", "数字饼干"] ]
# 大盘子 = []
#
# for 小盒子 in 饼干盒们:      # 第一层：遍历每个小盒子
#     for 饼干 in 小盒子:      # 第二层：遍历小盒子里的每块饼干
#         大盘子.append(饼干)  # 把饼干放进大盘子

#print(大盘子)
# 输出：['巧克力饼干', '草莓饼干', '奶油饼干', '动物饼干', '数字饼干']
# password = ""
# while password != "123456":  # 只要密码不是123456就继续问
#     password = input("请输入密码：")
# print("登录成功！")
# num = 1
# while num <= 5:  # 只要num≤5就继续
#     print(num)
#     num += 1     # 每次+1，直到num=6时停止
import pygame
pygame.init()

# 创建窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("打飞机")

# 玩家飞机
player = pygame.Rect(400, 500, 50, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 键盘控制移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5

    # 画画面
    screen.fill((0, 0, 0))  # 黑色背景
    pygame.draw.rect(screen, (255, 0, 0), player)  # 红色飞机
    pygame.display.update()

pygame.quit()


