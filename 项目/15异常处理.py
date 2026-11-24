# 异常处理
# 问题输入
try:
    print("========================")
    print(my_name)
    print("========================")
except NameError as e:
    print("输入出错,请联系管理员.异常信息:",e)
except ZeroDivisionError as e:
    print("0不饿能作为被除数.错误信息:",e)
# ----------------------------------------------------------------\
try:
    print("========================")
    print(1 / 0)
    print("========================")
except NameError as e:
    print("输入出错,请联系管理员.异常信息:",e)
except ZeroDivisionError as e:
    print("0不饿能作为被除数.错误信息:",e)
# ----------------------------------------------------------------\
try:
    print("========================")
    print("ABC"[10])
    print("========================")
except NameError as e:
    print("输入出错,请联系管理员.异常信息:",e)
except ZeroDivisionError as e:
    print("0不饿能作为被除数.错误信息:",e)
except IndexError as e:
    print("索引出现问题.错误信息:",e)

# 正常程序
try:
    print("========================")
    print("my_name")
    print("========================")
except NameError as e:
    print("输入出错,请联系管理员.异常信息:",e)
except ZeroDivisionError as e:
    print("0不饿能作为被除数.错误信息:",e)
    
    
# 焚诀
# ----------------------------------------------------------------\
try:
    print("========================")
    print(1 / 0)
    print("========================")
except Exception as e:
    print("程序运行出错了,请联系管理员.报错信息:",e)#Exception是所有异常的父类,他能包含所有异常.
finally:#(无论程序是否正常运行,这里面的代码都会运行)
    print("资源释放")
    
    # 异常传递
    # 异常的传递
def fun1():  
    print("fun1 ... running ...")
    fun2()

def fun2(): 
    print("fun2 ... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)

if __name__ == '__main__':
    try:    
        fun1()
    except Exception as e:
        print("程序出错了.",e)#为避免异常传递,在异常入口处捕获异常就可以了,就像这种嵌套函数是一级一级向调用它的函数传递异常,最终就会传到最下面主程序