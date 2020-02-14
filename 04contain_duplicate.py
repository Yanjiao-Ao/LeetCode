def containDuplicate(nums):
    return len(set(nums)) != len(nums)

li = [1,2,3,4,5,6,1]
print(containDuplicate(li))
