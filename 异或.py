def calculateXOR(n,m):
    sum = 0
    for i in range(n,m):
        sum = sum^i
        print(sum)

calculateXOR(0,8)
