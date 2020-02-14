def longestCommonPrefix(strs):
    res = ''
    count = []
    if len(strs) == 0:
        return res
    #找出字符串长度最小的
    for i in range(len(strs)):
        count.append(len(strs[i]))
    minIndex = count.index(min(count))
    for j in range(0,len(strs[minIndex])):
        for i in range(0,len(strs)):
            if strs[i][j] != strs[0][j]:
                return res#如果是break只是中断了内层的循环
        res += strs[0][j]
    return res






list = ["flower","flow","flight"]
print(longestCommonPrefix(list))
