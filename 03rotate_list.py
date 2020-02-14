#解法1：暴力循环
def rotate_list_1(nums,k):
    for i in range(0,k):#循环i次
        perv = nums[len(nums)-1]
        for j in range(0,len(nums)):
            temp = nums[j]
            nums[j] = perv
            perv = temp

    return nums

#测试样本
li=[1,2,3,4,5,6,7]
#print(rotate_list_1(li,3))
#解法二：切片
def rotate_list_2(nums,k):
    k %= len(nums)
    nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

#解法三：反转 [::-1]反转的意思
def rotate_list_3(nums,k):
    k %= len(nums)#这个是意思是因为没说k值一定比list的数量少。当k大于len（nums）时，除余
    nums.reverse()
    nums[:k] = nums[:k].reverse()
    nums[k:] = nums[k:].reverse()
    return nums
print(rotate_list_2(li,9))





