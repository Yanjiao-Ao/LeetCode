def onlyMissingNumber(A):
    hash = {}
    if len(A) == 0:
        return 1
    for i in range(len(A)):
        hash[A[i]] = 1
    print(hash)
    for i in range(1,len(A)+2):
        if i not in hash:
            return i
        else:
            continue


# def onlyMissingNumber_2(A):
#     head = 0
#     tail = len(A) -1
#     if len(A) == 0 or len(A) == 1:
#         return 1
#     A.sort()
#     value = len(A)//2
#     while head <= tail:
#         mid = (head + tail) //2
#         if A[mid] == value:
#             head = mid +1
#             value = value + (1/2)*value
#         elif A[mid] > value:


A = [2,3,1,5]
print(onlyMissingNumber(A))
