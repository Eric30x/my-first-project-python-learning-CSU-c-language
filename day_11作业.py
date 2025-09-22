# 1.定义一个函数abc(),需要传入2个参数:x,y, 实现计算:x**y,并且返回这个计算值,
# 用这个函数计算出,9的9次方的值,并且在函数外打印出这个值(函数调用与返回值接收)
# 2.用自己写好的这个abc函数,结合之前学过的map()映射函数,
# 计算2**3,3**4,4**5,5**6的值,并且将值保存到一个列表当中.
# def abc(x,y):
#     result=x**y
#     return result
# results = [abc(x, y) for x, y in [(2,3), (3,4), (4,5), (5,6)]]
# print( results)


# 3.用列表推导式,写出0-100(包含0和100)之内能被3整除的每个数字的平方再减1的值(例如:数字3则为3*3-1)
# result = [x**2 - 1 for x in range(101) if x % 3 == 0]
# print(result)
# 使用之前定义的abc函数
def abc(x, y):
    return x ** y
a= [(2, 3), (3, 4), (4, 5), (5, 6)]
# sults = list(map(lambda p: abc(p[0], p[1]), a))
# print(results)
# r
# e
a = list(map(abc, [2, 3, 4, 5], [3, 4, 5, 6]))
print(a)







