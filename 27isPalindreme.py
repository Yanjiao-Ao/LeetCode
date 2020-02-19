def isPalindrome(self,head):#因此最简单的方法就是将链表的值复制到数组列表中，再使用双指针法判断。
    val = []
    cur = head

    while cur:
        val.append(cur.val)
        cur = cur.next
    return val == val[::-1]
