#计算n的阶乘
# 递归调用 ----->一定得有终结点
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)
TEST = jc(10)
print(TEST)
# 案例二:案例2：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
# 具体规则如下：

# 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。

# 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def total_sum(discount,score,express,*args):
    total_sum = [goods[1]*goods[2] for goods in args]
    total_cost=sum(total_sum)
    
    if total_cost >= 5000 and discount <= total_cost:
            total_cost -= discount
    if total_cost >= 5000 and score//100 <= total_cost :
        total_cost -= score//100
    
   
    
    total_cost += express
    return total_cost
money = total_sum(100,6555,44.4,["鼠标",1000,2],["手机",5000,2])
print(money)