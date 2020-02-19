#  记录【今天之前买入的最小值】
#  计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
# 比较【每天的最大获利】，取最大值即可
def maxProfit(prices):
    if len(prices) == 0:#边界条件很重要！
            return 0
    miniprice = prices[0]
    max = 0
    for i in range(1,len(prices)):
        if prices[i] < miniprice:
            miniprice = prices[i]
        elif prices[i] - miniprice > max:
            max = prices[i] - miniprice
    return max




li = [7,1,5,3,6,4]
li2 = [7,6,4,3,1]
li3 = []
print(maxProfit(li3))
