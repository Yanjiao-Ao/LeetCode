def hasCycle(head):#我们可以通过检查一个结点此前是否被访问过来判断链表是否为环形链表。常用的方法是使用哈希表。
    hash = {}
    while head:
        if head in hash:
            return True
        else:
            hash[head] = 1
        head = head.next
    return False
