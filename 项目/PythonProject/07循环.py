# match循环
"""
num1 = float(input("first number: "))
num2 = float(input("second number: "))
coin = input("请输入运算符 (+ - * /): ")

match coin:
    case "+":
        print(f"{num1}+{num2}={num1+num2}")
    case "-":
        print(f"{num1}-{num2}={num1-num2}")
    case "*":
        print(f"{num1}*{num2}={num1*num2}")
    case "/":
        if num2 == 0:
            print("除数不能为 0")
        else:
            print(f"{num1}/{num2}={num1/num2}")
    case _:
        print("未知运算符")
"""
# while循环
"""
i=0
while i<10:
    print("1555")
    i += 1
else:
    print("循环结束")"""
# while习题
"""
total = 0
i = 1
while i<=100:
    if i%2==0:
        total += i
    i += 1
else:
    print(total)
"""
# for循环
"""
msg = input("请输入文字:")
for i in msg:#i是msg中的每一个字符
    print(i)
else:
    print("遍历结束")
"""
# for习题
"""
用法1: range(end) -> 获取一个从0开始，[到end结束（不含end）的整数序列]
  · range(5)获取的数据就是 0,1,2,3,4

用法2: range(start,end) -> 获取一个从[start开始，到end结束（不含end）的整数序列]
  · range(2,8)获取的数据就是 2,3,4,5,6,7

用法3: range(start,end,step) -> 获取[一个从start开始，到end结束（不含end），步长为step的整数序列]
  · range(0,10,2)获取的数据就是 0,2,4,6,8
  4.都不含 end：range(5) 是 0~4，range(2,8) 是 2~7，这是最常见的错误来源。
  5.range() 返回的不是列表，而是「range 对象」（可迭代），打印出来是 range(0, 5)。想看具体数字要转一下：print(list(range(5)))      # [0, 1, 2, 3, 4]
  6.range() 可以用来生成任意等差数列，甚至是负数等差数列：print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  7.step 可以是负数，用来倒着取：list(range(10, 0, -2))     # [10, 8, 6, 4, 2]
"""
"""
total = 0
for i in range(1,101):
    if i%2==1:
        total += i
print(total)    
"""
# 简化
"""
total = 0
for i in range(1,101,2):
        total += i
print(total)    
"""
# 案例2: 计算 100-500 之间所有3的倍数的数字之和
"""
total = 0  # 记录累加之和

for i in range(100, 501):
    if i % 3 == 0:  # i 是3的倍数
        total += i

print("100-500 之间所有3的倍数的数字之和： ", total)"""
# 嵌套循环
"""
m=int(input("请输入长度:"))
n=int(input("请输入宽度:"))
for i in range(n):
    for j in range(m):
        print("*",end="   ")
    print()
 """
#  嵌套循环:打印九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end="\t")
    print()
   """     
#    循环综合练习1
"""
m = ("请输入用户名:")
n = ("请输入密码:")
while True:#就算输出正确也会继续循环,所以要加break
    username = input(m)
    password = input(n)
    if username == "admin" and password == "123456":
        print("登录成功")
        break#关键字1:只能够跳出当前循环,如果有多层循环,只能够跳出当前循环(只能出现在循环中)
    elif username == "" or password == "":
         continue#关键字2:跳过当前循环,直接进入下一次循环(只能出现在循环中)
    else:
        print("用户名或密码错误，请重新输入")
        """
        # 循环综合练习2(猜随机数字比大小)
import random

random_num = random.randint(1, 100)  # 生成随机数

while True:
    # 接收输入的数字
    num = int(input("请输入一个数字："))

    # 比较
    if num > random_num:
        print("您输入的数字太大了！")
    elif num < random_num:
        print("您输入的数字太小了！")
    else:
        print("恭喜您，猜对了，666")
        break  # 跳出循环

print("随机生成的数字是：", random_num)