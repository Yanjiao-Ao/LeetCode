def solution(s):#求除有多少个不同的元音和多少个不同的辅音，然后排列组合。
    if len(s) <= 1:
        return 0
    dict_v = ['A','E','I','O','U']
    dict_c = ['Q','W','R','T','Y','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    v = set()
    c = set()
    # print(len(dict_c))
    # print(len(dict_v))
    for char in s:
        if char in dict_v:
            v.add(char)
        elif char in dict_c:
            c.add(char)
    num1 = 1
    num2 = 1
    for i in range(1,len(v)+1):
        num1 *= i
    for i in range(1,len(c)+1):
        num2 *= i
    return num1*num2

s = 'AABCY'
print(solution(s))
