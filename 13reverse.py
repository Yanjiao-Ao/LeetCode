def reverse(x):
    #{k:v for k, v in test_dict.items() if v>=3}
    #用string来做
    #判断正负：
    a = 1
    if x >= 0:
        a *= 1
    else:
        a *= -1
    str_x = str(a*x)
    temp = [a for a in str_x]
    temp.reverse()
    str_res = ''
    for i in range(len(temp)):
        str_res += temp[i]
    if a*int(str_res) < 2**31-1 and a*int(str_res) > -1*2**31:
         return a*int(str_res)
    else:
        return 0





x = -123237
print(reverse(x))
