#一段有n个台阶组成的楼梯，小明从楼梯的最低层向最高出前进，他可以选择一次迈一级台阶或者一次迈两级台阶。请问他有多少种不同的走法？（斐波拉契）
# 思路1: (0级台阶：1种走法)
# 	1级台阶：1种走法
# 	2级台阶：2种走法
# 	3级台阶：3种走法
# 	4级台阶：5种走法
# 	5级台阶：8种走法
#
# 思路2：假设n(n > 2)级台阶有F(n)种走法，则第一次迈一步时有F(n-1)总种走法，第一次迈两步时有F(n-2)种走法，则F(n) = F(n-1) + F(n-2)。F(1) = 1, F(2) = 2

def climbStairs_1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return climbStairs_1(n-1) + climbStairs_1(n-2)

def climbStairs_2(n):
    list = [1,1]

    for i in range(2,n+1):
        list.append(list[i-1] + list[i-2])
    print(list)
    return list[n]

def climbStairs_3(n):#时刻考虑边界条件
    a = 1
    b = 1
    c = 0
    if n == 0 or n == 1:
        return 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c

print(climbStairs_3(9))

