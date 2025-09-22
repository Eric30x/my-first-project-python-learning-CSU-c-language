# 1.请用索引的方式将下面列表中'abcd' 与 '上山打老虎' 2个元素位置互调
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# a[3]='上山打老虎'
# a[5]='abcd'
# print(a)
# 2.请将下面列表中的元素,分为2个不同类型(分别是数字类型(包含整数类型和浮点数类型) 和 字符串类型)
# 并且分别保存到2个不同的自己创建的空列表当中,用代码实现
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
int_box=[]
str_box=[]
for i in a:
    if type(i)==int:
        int_box.append(i)
    elif type(i)==str:
        str_box.append(i)
    elif type(i)==float:
        int_box.append(i)
print(int_box)
print(str_box)









































