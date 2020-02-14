#解法一：遇到零移除，记录移走了多少个，最后统一加在末尾
def moveZeroes_1(nums):
    count = 0
    for i in range(-len(nums),0):
        if nums[i] == 0:
            nums.remove(nums[i])
            count +=1
    for j in range(count):
        nums.append(0)
    return nums
#解法二：双指针
def moveZeroes_2(nums):
    i = 0#指非零元素更新到的位置
    j = 0#遇到非零就和i位置更新，遇到零就跳过
    while j < len(nums) and i < len(nums):
        if nums[j] == 0:
            j += 1
        else:#if nums[j] != 0
            nums[i] = nums[j]
            i += 1
            j += 1
    for x in range(i, len(nums)):
        nums[x] = 0
    return nums




li = [1,0,3,12,0,1]
print(moveZeroes_2(li))


