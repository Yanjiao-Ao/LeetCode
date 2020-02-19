def merge_1(nums1,m,nums2,n):
    nums1[:] = sorted(nums1[:m]+nums2)

def merge_2(nums1,m,nums2,n):
    i = 0
    j = 0
    nums1_copy = nums1[:m]
    nums1[:] = []
    while i < m and j < n:
        if nums1_copy[i] <= nums2[j]:
            nums1.append(nums1_copy[i])
            i += 1
        else:#nums1_copy > nums2[j]
            nums1.append(nums2[j])
            j += 1
    if i < m:
        nums1[i+j:] = nums1_copy[i:]
    if j < n:
        nums1[i+j:] = nums2[j:]
