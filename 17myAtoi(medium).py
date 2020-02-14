def myAtoi(s):
    #用hashmap来筛出符合条件的
    str_num = ''
    sign = 1
    numlist = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}#可以换成isdigit,但是速度没有hashmap快
    if s == None:
        return 0

    flag = 0 #一旦开始加数字了，一旦数字结束后面的所有都没用
    for i in range(len(s)):
        if s[i] == ' ' and flag == 0 :
            continue
        elif s[i] in ('+','-') and flag == 0:
            if i+1 < len(s) and s[i+1] not in numlist:# 排除'+' '-' 后面不是一位是数字的情况
                return 0
            else:
                if s[i] == '+':
                    sign *= 1
                    continue
                else:# s[i] == '-'
                    sign *= -1
                    continue
        elif s[i] in numlist:
            str_num += s[i]
            flag = 1
        else:
            break

    if len(str_num) == 0:
        return 0
    else:
        int_num = sign*int(str_num)
        if int_num >= 2**31:
            return 2**31 -1
        elif int_num < -1*2**31:
            return -1*2**31
        else:
            return int_num



s1 = "-4193 with words 090"
s2 = "   -42 123"
s3 = "42"
s4 = "words and 987"
s5 = "words and "
s6 = '   -   '
s7 = ' '
print(myAtoi(s1))
print(myAtoi(s2))
print(myAtoi(s3))
print(myAtoi(s4))
print(myAtoi(s5))
print(myAtoi(s7))
