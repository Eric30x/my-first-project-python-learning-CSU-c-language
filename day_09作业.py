#  作业1: b = [5, 6, 7, '吃鸡',8, 9 ,'王者荣耀']
#  首先,把列表b变成1个迭代器,然后把这个迭代器里的元素一个个取出,
#  (结合while循环和next()函数)
# 如果是数字,则(数字*2+1)打印后输出,如果是字符串,则把字符串跳过,循环结束后不允许报错
# b = [5, 6, 7, '吃鸡',8, 9 ,'王者荣耀']
# a=iter(b)
# while True:
#     try:
#         item=next(a)
#         if type(item)==int:
#             print(item*2+1)
#     except StopIteration:
#         break
    # if item==5or item==6or item==7or item==8or item==9:
    #     print(item*2+1)
    # if type(item)==str:
    #     continue
# while True:
#     try:
#         item = next(my_iterator)
#         print(item)
#     except StopIteration:
#         break  # 迭代结束，退出循环

# 作业2:利用map函数和sum函数 依次计算[1,2,3,4,5,6]的和 再加100 的值
#                  [2,3,4,5,6,7]的和 再加200 的值
#                  [3,4,5,6,7,8]的和 再加300 的值

# 自己创造符合要求的数据结构作为map函数参数,再利用map函数计算,再通过for循环依次把3个结果打印出来

A=[([1,2,3,4,5,6],100),([2,3,4,5,6,7],200),([3,4,5,6,7,8],300)]
def 计算(z):
    x,y=z
    return sum(x)+y
结果=map(计算,A)
for i in 结果:
    print(i)
# def 计算:
#     return
# A=a[0]*100+sum(a) and b[0]*100+sum(b) and c[0]*100+sum(c)
# print(A)



