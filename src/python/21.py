# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        pre = None
        p1 = l1
        head = l1
        p2 = l2
        while p2:
            while p1 and p2.val > p1.val:
                pre = p1
                p1 = p1.next
            if not pre:
                pre = p2
                p2 = p2.next
                pre.next = p1
                head = pre

            else:
                pre.next = p2
                p2 = p2.next
                pre.next.next = p1
                pre = pre.next
        return head

x1 = ListNode(1)
x2 = ListNode(2)
a = Solution()
b = a.mergeTwoLists(x2, x1)
print(b.val)
print(b.next.val)