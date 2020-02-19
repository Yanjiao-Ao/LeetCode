def smallestUnexist(A:list):
    a = max(A)
    if a <= 0:
        return 1
    hash = {}
    for i in range(1,a+2):
        hash[i] = 0
    for i in range(len(A)):
        if A[i] <= 0:
            continue
        elif A[i] in hash:
            hash[A[i]] += 1
    for i in hash:
        if hash[i] == 0:
            return i



A = [1, 2, 3]
li = [0, 3, 6, 4, 1, 2]
print(solution(li))
