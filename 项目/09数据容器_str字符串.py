# 字符串 基本操作 ---> 不可变的(无法修改)、有序性、可迭代性
s = "Hello-Python"


print(s[4])  # 正向索引
print(s[-8])  # 反向索引


for i in s:
    print(i)


# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])
print(s[6::1])

# 步长 --> 正数: 从前往后截取 ；负数: 从后往前截取 (若步长为负数, 则起始索引必须大于结束索引)
print(s[-8::-1])