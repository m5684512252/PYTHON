# 案例:邮箱格式的验证(包含一个@和至少一个.)
mail = input("请输入邮箱地址:")
if mail.count("@")==1 and mail.count(".")>=1:
    print("邮箱格式正确")
else:
    print("邮箱格式不正确")
# 方式2:in运算符
mail = input("请输入邮箱地址:")
if mail.count("@")==1 and "." in mail:
    print("邮箱格式正确")
else:
    print("邮箱格式不正确")