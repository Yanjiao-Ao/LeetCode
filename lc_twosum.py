def two_sum(list,target):
    head = 0
    tail = len(list) - 1
    sum = list[head] + list[tail]
    while head <= tail:
        if sum == target:
            return list.index(list[head]),list.index(list[tail])
        elif sum > target:
            tail -= 1
        else: #sum < target
            head +=1
            



li = [2,7,11,15]
print(two_sum(li,9))
