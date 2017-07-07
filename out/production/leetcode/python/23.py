from heapq import heappop, heappush

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = filter(lambda x: x, lists)
        heap = []
        for t in lists:
            heappush(heap, (t.val, t))
        head = None
        curr = head
        while heap:
            v, t = heappop(heap)
            if not head:
                head = t
                curr = head
            else:
                curr.next = t
                curr = curr.next
            t = t.next
            if t:
                heappush(heap, (t.val, t))
        return head

a = Solution()
head = ListNode(0)
head.next = ListNode(2)
head.next.next = ListNode(5)
b = a.mergeKLists([head])
print(b)