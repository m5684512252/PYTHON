# 列表 -list (1.可存储不同类型的元素2.元素有序,可以重复,可以修改)
"""
s=[1,2,3,4,5,6,7,8,9]#列表示例(索引从0开始,如反向索引从-1开始)

# 获取列表中的元素
print(s[0])#正向索引,获取第一个元素
print(s[-9])#反向索引,获取第一个元素
print(s[5]) #正向索引,获取第六个元素
print(s[-4])#反向索引,获取第六个元素


# 修改
s[5]="AAA"
print(s)
#索引超出范围,程序会报错:list assignment index out of range
# s[10]="BBB"
# print(s) 

# 删除
del s[5]
print(s)

# 添加元素
s.append("CCC")
print(s)
# 遍历
for i in s:
    print(i)
    # 切片
    s=[1,2,3,4,5,6,7,8,9]
print(s[0:5:1])#获取索引0-4的元素
print(s[0:5])#获取索引0-4的元素
print(s[:5])#获取索引0-4的元素
print(s[5])#不能省略第一个冒号
print(s[0:-2:1])#获取索引0-6的元素(反向索引)
print(s[-1:-3:-1])#从后往前的切片(反向索引)
"""
"""
# ----------------- 列表 list 常用方法 ---------------------------
# 列表定义
s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
print(s)


# append(): 在列表尾部追加元素
s.append(188)
print(s)


# insert(): 在指定索引之前，插入元素
s.insert(2, 80)
print(s)


# remove(): 移除列表中第一个匹配到的元素
s.remove(90)
print(s)


# pop(): 删除列表中指定索引位置的元素并返回(如果未指定，默认删除最后一个)
e = s.pop(1)
print(e)


e = s.pop()
print(e)


print(s)


# sort(): 排序
s.sort()
print(s)


# reverse(): 反转列表元素
s.reverse()
print(s)
"""

# 案例
"""
s = []
for i in range(10):
    num = int(input("请输入一个整数:"))
    s.append(num)
print(s)
s.sort()
print(s)#排序
print(s[-1])#最大值
print(s[0])#最小值
# sum()函数:求和 len()函数:求长度
print(sum(s)/len(s))#平均值
"""

# 案例二
"""
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

for i in num_list2:
    num_list1.append(i)
print(num_list1)
num_list1.sort()
print(num_list1)
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(new_list)
"""

# 案例二(简化版)
"""
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# 1.合并两个列表(解包)
num_list=[*num_list1,*num_list2]#解包*(将列表解开为单独的元素)
print(num_list)

num_list1.sort()
print(num_list1)
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(new_list)
"""

# 案例二(极简版)
"""
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

num_list = num_list1+num_list2#列表相加(合并两个列表)
print(num_list)
num_list1.sort()
print(num_list1)
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(new_list)
"""
