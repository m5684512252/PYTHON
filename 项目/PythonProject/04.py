# type()#查看自变量类型
import numbers
from operator import truediv

print(type(100))
print(type(False))
print(type(3.14))
print(type(None))
print(type(True))





numbers=-100
print(type(numbers))

#isinatance(数据,类型)如果是返回true 不是反false
print(isinstance(numbers,int))
print(isinstance(numbers,float))
print(isinstance(numbers,str))

