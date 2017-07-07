# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        first = head
        second = first.next if first else None
        curr = second.next if second else None
        while first and second:
            if not pre:
                head = second
                second.next = first
                first.next = curr
            else:
                pre.next = second
                second.next = first
                first.next = curr
            pre = first
            first = pre.next
            second = first.next if first else None
            curr = second.next if second else None
        return head

a = Solution()
l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
c = a.swapPairs(l)
print(c)