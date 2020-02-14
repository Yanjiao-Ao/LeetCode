#解法一：暴力循环
def twoSum_1(nums,target):
    for i in range(len(nums)):
        diff = target -nums[i]
        for j in range(i+1,len(nums)):
            if nums[j] == diff:
                return [i,j]
#解法二：哈希表
def twoSum_2(nums,target):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = i#value值是index，因为最后要返回的是index，如果key位index，最后的返回不好写
    for j in range(len(nums)):
        diff = target - nums[j]
        if diff in hash and hash[diff] != j:#找的差值的那个数不能是它本身
            return [j, hash[diff]]





li = [2,7,11,15]
print(twoSum_2(li,9))

