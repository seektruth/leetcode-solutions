# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
       self.val = x
       self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ids_A = set()
        c = headA
        while c:
            ids_A.add(id(c))
            c = c.next
        c = headB
        while c:
            if id(c) in ids_A:
                return c
            c = c.next
        return None

a =Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a1.next = a2
print(a.getIntersectionNode(a1,a2))