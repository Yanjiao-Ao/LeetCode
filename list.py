list = [{'id':1001,'name':'zhangsan','age':20},
        {'id':1002,'name':'lisi','age':25},
        {'id':1004,'name':'wangwu','age':27},
        {'id':1007,'name':'zhaoliu','age':33}]

def bin_search(list,id):
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high)//2
        if list[mid]['id'] == id:
            return mid

        elif list[mid]['id'] > id:
            low = mid + 1
        else: #list[mid]['id'] < id
            high = mid - 1

    return -1

print('The Index:',bin_search(list,1002))
print(list[bin_search(list,1002)])
