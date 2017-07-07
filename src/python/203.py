# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        front = None
        current = head
        nex = head.next if head else None
        while current:
            if current.val == val:
                if front:
                    front.next = nex
                else:
                    head = nex
            else:
                front = current
            current = nex
            nex = head.next if head else None
        return head



