# # 定义函数
# # def 函数名(参数列表):
# #      函数体
# #     ....
# #     return 返回值
# # 函数名(参数)调用函数
# # 求圆的面积
# def circle_area(radius):
#     area = 3.14 * radius * radius
#     return area
# r = float(input("请输入圆的半径:"))
# area = circle_area(r)
# print(area)
# # 求矩形面积
# def rectangle_area(length, width):
#     area = length * width
#     return area
# l = float(input("请输入矩形的长:"))
# w = float(input("请输入矩形的宽:"))
# area = rectangle_area(l, w)
# print(area)
# # 计算圆的面积和周长
# def circle(radius):
#     return 3.14*radius**2,2*3.14*radius#元组
# r = float(input("请输入圆的半径:"))
# sl = circle(r)#值封装到元组中
# print(sl)
# area,perimater = circle(r)#解包
# print("面积:",area)
# print("周长:",perimater)
# # 函数说明文档
# # 函数2：计算长方形的面积 -- 长，宽
# def rectangle_area(l,w): 
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area

# help(rectangle_area)
# # 函数的嵌套和调用(def后面带缩进的未定义函数的调用是延时调用,到后面真正调用时如果前面函数被定义了,那就可以被成功调用)
# def function_a():        
#    print("a ... before")
#    function_b()
#    print("a ... after")

# def function_b():        
#    print("b ... before")
#    function_c()
#    print("b ... after")

# def function_c():        
#   print("c ...")

#   function_a() 
# 案例1 计算三角形面积
# def triangle(x,h):
#     return x*h/2
# long = int(input("请输入长度:"))
# high = int(input("请输入高度:"))
# s = triangle(long,high)
# print(s)
# # 案例二 定义也个函数,计算传入字符串中元音字母的个数
# def count_aeiou(s):
#     NUM = 0
#     for w in s:
#         if w in "aeiouAEIOU":
#             NUM += 1
#     return NUM
# sentence = input("请输入英文句子:")
# print(count_aeiou(sentence))     

# 案例三 定义一个函数计算传入班级学员成绩列表的最高分,最低分,平均分(保留一位小数),并返回(round()是保留一位小数)
def score(score_list):
    max_score=max(score_list)
    min_score=min(score_list)
    averge_score=sum(score_list)/len(score_list)
    return(max_score,min_score,averge_score)
list=[]
for i in range(10):
    list.append(int(input("分数:")))
max,min,avg=score(list)
print(max,min,avg)