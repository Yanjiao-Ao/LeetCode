def countAndSay(n):
    if n ==1:
        return '1'#申明一个起始变量
    input = countAndSay(n-1)
    i = 0 #count different
    j = 1
    output = ''
    while i+j < len(input):
        if input[i] == input[i+j]:
            j += 1
        else:#str[i] != str[j]
            output = output + str(j) + input[i]
            i = i + j
            j = 1 #count number
    output = output + str(j) + input[i]
    return output


n = 5
print(countAndSay(n))
