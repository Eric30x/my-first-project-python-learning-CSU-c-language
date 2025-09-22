# 1. 必做题:分别用普通函数和匿名函数实现一个能够鉴别 某2个数的乘积是否为3的倍数 的函数 ,
#    如果是3的倍数,则返回这2个数的乘积,如果不是3的倍数,则返回None
distingguish=lambda x,y:print(x*y) if x*y%3==0 else 'None'
print(distingguish(3,4))
def distingguish(x,y):
    if x*y%3==0:
        pass
        return x*y
    else:
        return 'None'
print(distingguish(2,4))

#

# 2. 选做题:用递归求一个全部都是数字的列表的和 lyst = [1, 2, 3, 5, 7, 9]


# 3. 完成以下递归处理多层嵌套结构的递归流程注释（示例就是上课的递归计算阶乘的流程）
from collections.abc import Iterable


def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, Iterable): # 判断是否可迭代且不是字符串
            result.extend(flatten(item))  # 递归展开
        else:
            result.append(item)  # 不是可迭代的元素直接添加
    return result
# # 示例
nested_list = [1, 2, [3, 4, [5, 6]]]
flattened_list = flatten(nested_list)
print(flattened_list)
#
# #把怎么递归的注释写在下面