# -------------------------------------------------- 函数 - 变量的作用域 --------------------------------------------------
# 全局变量
num = 100


# 定义函数
def circle_area(r):  # 1个用法
    # 局部变量(只能在函数内部使用)
    pi = 3.14
    area = pi * r * r
    return area

print("pi = ")


# 调用函数

c_area = circle_area(10)
print(c_area)
# global 在局部变量中要用全局变量时(这样在局部变量中定义的值就会同步到全局变量中)
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 传参方式一：位置参数
stu = reg_stu("张三", 18, "男", "北京")
print(stu)


# 传参方式二：关键字参数
stu = reg_stu(name="王林", age=28, gender="男", city="北京")
print(stu)

stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
print(stu)


# 传参方式三：位置参数 + 关键字参数 -> 位置参数在前，关键字参数在后
stu = reg_stu("李慕婉", 20, gender="女", city="北京")
print(stu)
# 如果在函数中直接加入参数就是默认参数即def reg_stu(name,age.gender+"男",city="北京")
# *args不定长参数(元组)位置参数
def cal(*args):
    max_data = max(args)
    min_data = min(args)
    ave_data = sum(args)/len(args)
    return max_data,min_data,round(ave_data,1)

print(cal(12,15,15,6,44,4,54,46,46,41))

#**kwargs 不定长参数的关键字参数
def cal(*args,**kwargs):
    max_data = max(args)
    min_data = min(args)
    ave_data = sum(args)/len(args)
    print(kwargs)
    if kwargs.get("round") is not None:
        ave_data = round(ave_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值:{min_data},最大值:{max_data},平均值:{ave_data}")
    return max_data,min_data,ave_data
    
print(cal(12,15,1,1,111,145,44,round=3))
print(cal(12,15,15,6,44,4,54,46,46,41))
# 参数的类型
# 普通参数:数字,布尔,字符串等
# 特殊参数:函数
def add(x,y):
    return x+y
def multiply(x,y):
    return x/y

def calc(x,y,oper):#oper是形式参数,表示的是函数
    return oper(x,y)#以输入的函数来计算

print(calc(10,20,add))

# 匿名函数
# 匿名函数指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写（单行表达式）
# 定义匿名函数(会自动return 代码里不用写return)
# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序 ；
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)


data_list.sort(key=lambda item : len(item)) # 匿名函数典型的应用场景 .
print(data_list)
