def strStr_1(haystack,needle):#双指针
    if len(needle) == 0:#判断特殊条件
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)+1-len(needle)):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            else:
                if j == len(needle):
                    return i
        return -1


def strStr_2(haystack,needle):#
    if len(needle) == 0:#判断特殊条件
        return 0
    if needle not in haystack:
        return -1
    else:
        for i in range(0,len(haystack)+1 - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i
        else:
            return -1
def strStr_3(haystack,needle): #一句话搞定检测 # 熟悉字符串的内嵌函数
    # str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
    return haystack.find(needle)





haystack = "hello"
needle = "ll"
print(strStr_1(haystack,needle))
