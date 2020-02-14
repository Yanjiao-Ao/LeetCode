#hashMap
def intersect(nums1,nums2):
    dict = {}
    intersect =[]
    for i in nums1:
        if i not in dict:
            dict[i] = 1
        else:#if i in dict
            dict[i] += 1
    for j in nums2:
        if j in dict:
            if dict[j] > 0:#当value变为0时就不考虑，把这个条件给筛出去
                dict[j] -= 1
                intersect.append(j)

    return intersect




nums1 = [4,9,4]
nums2 = [4,5,2,7,9,4]
print(intersect(nums1,nums2))


