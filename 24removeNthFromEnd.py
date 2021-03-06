# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        first = dummyHead
        second = dummyHead

        for i in range(n+1):
            first = first.next

        while first != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummyHead.next



