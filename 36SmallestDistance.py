def solution(A):
    if len(A) == 0:
        return 0
    list = []
    for p in range(1,len(A)):
        sum1 = 0
        sum2 = 0
        for i in range(0,p):
            sum1 += A[i]
        for j in range(p,len(A)):
            sum2 += A[j]
        list.append(abs(sum1 - sum2))
    return min(list)

def solution_2(A):
    if len(A) == 0:
        return 0
    res_list = []
    sum = 0
    for num in A:
        sum += num
    sum1 = 0
    for p in range(0,len(A)-1):
        sum1 += A[p]
        res_list.append(abs(sum-2*sum1))
    return min(res_list)

A=[3,4]

print(solution_2(A))
