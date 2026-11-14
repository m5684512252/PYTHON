# # 定义字符串三种方式
# s1 ="hello"#双引号定义
# s2='python'#单引号定义
# s3="""
# Hello:
# 欢迎大家进入~
# """#三引号定义(多行字符串)
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))
#
# # 定义字符串It's very good
# # 转义字符\' \" \n \t
# msg='It\'s very good'
# print(msg)
#
# msg2="It's very good"
# print(msg2)
#
# msg3='我是"谁"'
# print(msg3)
#
# msg4="我是\"谁\""
# print(msg4)
#
# print("\t欢迎大家进入Python课程的学习!\n\t大家记得一件三连哦")


# 字符串的拼接
s="人生苦短""我用python"
print(s)

b1="人生苦短"
b2="我用"
print("归属说:"+b1+","+b2)

name="姓名"
age="18"
profession="专业"
hobby="爱好"
print("大家好,我是"+name+",今年"+age+",学习的专业是"+profession+",爱好"+hobby)#如果字符类型不符合需要先转换字符类型 例:str(变量名)

#字符串格式化   %s 占位符
name="姓名"
age="18"
profession="专业"
hobby="爱好"
print("大家好,我是%s,今年%s,学习的专业是%s,爱好%s"%(name,age,profession,hobby))#如果字符类型不符合需要先转换字符类型

# 字符串格式化  方式二:f"..{变量名/表达式}.."  推荐方式






























