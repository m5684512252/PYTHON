# 输入与输出----input()
"""
name=input("请输入你的姓名")
age=input("请输入您的年龄")

print(f"你的名字是{name},年龄是{age}")
"""

# +加法 1+5
# -减法 8-3
# *乘法 3*8
# /除法 10/5结果为小数
# //整除 10//3整除结果为整数
# %取余 10%3 结果为1
# **幂指数 10**3 10的三次方

#算数运算符优先级-->**-->*/ // % --> +  -
"""
print("0.1+10/4**2= ",0.1 + 10 / 4 ** 2)
"""
# 赋值运算符
# =  赋值运算符 num+=2 等效于num=num+2
# += 加法赋值运算符 num-=2 等效于num=num-2
# -= 减法赋值运算符 以下同上
# *=乘法赋值运算符
# /=除法赋值运算符
# %=取模赋值运算符
# //=取整除赋值运算符
# **=幂赋值运算符
"""
num = 85

num += 10  # num = num + 10
print("num += 10 后, num = ", num)  # 95

num -= 10  # num = num - 10
print("num -= 10 后, num = ", num) # 85

num *= 10  # num = num * 10
print("num *= 10 后, num = ", num) # 850

num /= 10  # num = num / 10
print("num /= 10 后, num = ", num) # 85.0

num //= 10 # num = num // 10
print("num //= 10 后, num = ", num)# 8.0

num %= 3  # num = num % 3
print("num %= 3 后, num = ", num)# 2.0

num **= 3  # num = num ** 3
print("num **= 3 后, num = ", num)# 8.0
"""
# 比较预算符
# == 等于
# != 不等于
# > 大于
# >=大于等于
# < 小于
# <= 小于等于
"""
print("100 == 100 吗 : ", 100 == 100)  #True
print("'100' == '100' 吗 : ", "100" == "100")  #True
print("100 != 100 吗 : ", 100 != 100)  #False

print("100 < 100 吗 : ", 100 < 100)  #False
print("100 <= 100 吗 : ", 100 <= 100)  #True

print("100 > 100 吗 : ", 100 > 100)  #False
print("100 >= 100 吗 : ", 100 >= 100) #True
"""
# 逻辑运算符
# and 与(并且) 都要符合
# or 或(或者) 只有一个符合即可
# not 非(相反) 取反操作

# if语法
# if elif(可用多个) else否则
"""
score = int(input("your score:"))
if score>=85:
    print("excellent")
elif score<=85 and score>=60:
    print("good")
else:
    print("not good")
"""
#打折
"""
money=int(input("金额"))
if money>=500:
    money=money*0.8
    print(money)
elif money>=300 and money<500:
    money=money*0.9
    print(money)
elif money>=100 and money<=300:
    money=money*0.95
    print("money")
else:
    print(money)
"""
"""
# 案例
a = int(input("请输入第一个边的边长"))
b = int(input("请输入第二个边的边长"))
c = int(input("请输入第三个边的边长"))

if a+b>c and a+c>b and b+c>a:#条件成立,构成三角形
    if a ==b and b==c:
        print(f"{a} {b} {c}这三个边构成等边三角形")
    elif a==b or b==c or c==a:
        print(f"{a} {b} {c}这三个边构成等腰三角形")
    else:
        print(f"{a} {b} {c}这三个边构成普通三角形")
else:
      print(f"{a} {b} {c}这三个边不能构成三角形!!!")
"""











