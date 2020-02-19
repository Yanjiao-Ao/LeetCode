# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList_1(self, head: ListNode) :
        p,q,r = head, head.next,head.next.next
        p.next = None
        q.next = p

        if not head:#如果head为null
            return #None可以省略
        if not head.next:
            return head
        if not head.next.next:
            p.next = None
            q.next = p

        while q:#就是q的node还有值，不为null的时候
            p = q
            q = r
            r = r.next
            q.next = p

    def reverseList_2(self,head:ListNode):
        tmp = None#存储功能
        pre = None
        while head != None:
            tmp = head.next
            head.next = pre
            pre = head#移动到下一个点
            head = tmp

