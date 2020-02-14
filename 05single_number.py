#异或算法：
def singleNumber_1(nums):
    a = 0
    for num in nums:
        a ^= num
    return a

#解法二：遍历
def singleNumber_2(nums):
    no_duplicate_list = []
    for num in nums:
        if num not in no_duplicate_list:
            no_duplicate_list.append(num)
        else:
            no_duplicate_list.remove(num)
    return no_duplicate_list.pop()


li = [1,1,3,3,4,4,5]
print(singleNumber_2(li))
