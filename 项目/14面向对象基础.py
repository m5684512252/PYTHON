# 类与对象(大驼峰命名法,每个单词首字母大写,单词间没有分隔符)
# 不推荐方式
class Car:
    pass
cl = Car()
cl.color = "red"
cl.brand = "BMW"
print(cl)
print(cl.__dict__)#将所有的信息以字典的方式输出
print(cl.color)

# 推荐方式
class Car:#__init__方法是初始化的方法,会在对象创建时自动调用,可在该方法中为对象设置对应的属性
    # self:是第一个参数,表示当前创建出来的实例对象
    def __init__(self,c_brand,c_color,c_name,c_price):
        self.brand = c_brand
        self.color = c_color
        self.name = c_name
        self.price = c_price
# 创建对象
cl = Car("Benz","sliver","G63",1200000)
print(cl)
print(cl.__dict__)
print(cl.brand)

# 实例方法
class Car:#__init__方法是初始化的方法,会在对象创建时自动调用,可在该方法中为对象设置对应的属性
    # self:是第一个参数,表示当前创建出来的实例对象
    def __init__(self,c_brand,c_color,c_name,c_price):
        self.brand = c_brand
        self.color = c_color
        self.name = c_name
        self.price = c_price
# 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶中......")
    
    def total_cost(self,discount,rate):
        total_cost = self.price*discount + self.price*rate
        return total_cost
    
# 创建对象
cl = Car("Benz","sliver","G63",1200000)
print(cl)
print(cl.__dict__)
print(cl.brand)
cl.running()          # 只打印那句话
print(cl.total_cost(0.8,0.1))



# 魔法方法(不用自己调用,解释器自动调用)
class Car:#__init__方法是初始化的方法,会在对象创建时自动调用,可在该方法中为对象设置对应的属性
    # self:是第一个参数,表示当前创建出来的实例对象
    def __init__(self,c_brand,c_color,c_name,c_price):
        self.brand = c_brand
        self.color = c_color
        self.name = c_name
        self.price = c_price
# 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶中......")
    
    def total_cost(self,discount,rate):
        total_cost = self.price*discount + self.price*rate
        return total_cost
# 定义魔法方法
    def __str__(self):
        return f"{self.brand} {self.color} {self.name}"
    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand
    def __lt__(self,other):
        return self.price < other.price
    
    
# 创建对象
c1 = Car("Benz","red","G63",1200000)
c2 = Car("Benz","sliver","G63",1200001)
print(c1)
print(c1 == c2)
print(c1 < c2)

#属性(实例属性/类属性)
class Car:#__init__方法是初始化的方法,会在对象创建时自动调用,可在该方法中为对象设置对应的属性
    #类属性(用于整个类中的属性)整个类普遍的
    wheel= 4
    tax_rate=0.1
    
    # self:是第一个参数,表示当前创建出来的实例对象
    def __init__(self,c_brand,c_color,c_name,c_price):
        #实例属性(实例属性里的值优先,若没有实例属性,则识别类属性)各个对象特有的
        self.brand = c_brand
        self.color = c_color
        self.name = c_name
        self.price = c_price
 
# 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶中......")
    
    def total_cost(self,discount,rate):
        total_cost = self.price*discount + self.price*rate
        return total_cost
# 定义魔法方法
    def __str__(self):
        return f"{self.brand} {self.color} {self.name}"
    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand
    def __lt__(self,other):
        return self.price < other.price
    
    
# 创建对象
c1 = Car("Benz","red","G63",1200000)
c2 = Car("Benz","sliver","G63",1200001)
print(c1)
print(c1 == c2)
print(c1 < c2)
print(c1.wheel)
# 通过类名访问类属性
print(Car.wheel)