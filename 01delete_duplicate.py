def delete_duplicate(nums):#解题思路：双指针；优化，如果存在一个没有重复数的列，会多话时间，所以直接
    head = 0
    tail = 1
    if len(nums) ==0:
        return 0
    if len(nums) == 1:
        return 1
    while(tail<len(nums)):
        if nums[head] != nums[tail]:
            nums[head +1] = nums[tail]
            head +=1
            tail +=1
        else:#nums[q] == nums[p]
                tail +=1
    return head + 1

li = [0,0,1,1,1,2,2,3,3,4]
print(delete_duplicate(li))
