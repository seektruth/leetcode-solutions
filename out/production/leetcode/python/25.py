# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def reverse_single(s_list):
            ne = None
            current = s_list
            while current:
                if not ne:
                    ne = current
                    current = current.next
                    ne.next = None
                    tail = ne
                else:
                    t = current.next
                    current.next = ne
                    ne = current
                    current = t
            return ne, tail

        new_head = None
        tail = new_head
        cache = None
        curr = head
        i = 0
        while curr:
            if not cache:
                cache = curr
                curr = curr.next
                cache.next = None
                t = cache
            else:
                t.next = curr
                t = curr
                curr = curr.next
                t.next = None
            i += 1
            if i == k or not curr:
                if i == k:
                    cache, t = reverse_single(cache)
                if not new_head:
                    new_head = cache
                else:
                    tail.next = cache
                tail = t
                cache = None
                i = 0
        return new_head

a = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
c = a.reverseKGroup(None,1)
print(c)