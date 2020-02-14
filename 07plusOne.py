#坑：考虑数很大的时候会溢出，然后可以直接从list转成str
#解法一
def plusOne(digits):
    res = []
    #可以直接转成string型
    str_digits = ''
    for i in range(len(digits)):
        str_digits += str(digits[i])
    str_sum = str(int(str_digits)+1)
    for i in range(0,len(str_sum)):
        res.append(int(str_sum[i]))
    return res


#解法二
#def plusOne(self, digits: List[int]) -> List[int]:
        #return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))


list = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3]
print(plusOne(list))
