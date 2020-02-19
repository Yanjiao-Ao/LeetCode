class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwoLists(self,l1,l2):
        prehead = ListNode(-1)
        p = prehead
        while l1 and l2:#就是while l1 != None and l2 != None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:#l1.val > l2.val
                p.next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 if l1 is not None else l2#!!!!
        return prehead.next
