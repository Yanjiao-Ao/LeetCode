def maxProfit(prices):
    profit = 0
    for i in range(1,len(prices)):
        temp = prices[i] - prices[i-1]
        if temp > 0:
            profit = profit + temp
    return profit

li = [7,1,4,3,5]
print(maxProfit(li))
