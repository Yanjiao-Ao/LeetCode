def isBadVersion(version):
    bad = 8
    #return bool(version == bad)#bool用法：返回一个条件正确与否，比如a < b
    if version < bad:
        return False
    else:
        return True
def isFirstBadVersion(n):
    head = 1
    tail = n
    while head <= tail:
        mid = (head+tail)//2#要在循环里面
        if isBadVersion(mid) == False:
            head = mid + 1
        elif isBadVersion(mid) == True:
            tail = mid - 1
    return head

print(isFirstBadVersion(9))
for i in range(1,10):
    print (isBadVersion(i))
