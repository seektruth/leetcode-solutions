class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        MAX = 1 << 31
        MIN = -1 * MAX
        if not nums1 and not nums2:
            return 0
        if len(nums2) > len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        l1 = len(nums1)
        l2 = len(nums2)
        if l1 + l2 < 2:
            return nums1[0]
        nums1.insert(0, 0)
        nums2.insert(0, 0)
        lo = (l1 - l2) / 2
        hi = (l1 + l2) / 2
        t1 = (lo + hi) / 2
        t2 = (l1 + l2) / 2 - t1
        while True:
            left1 = nums1[t1]
            left2 = nums2[t2] if t2 > 0 else MIN
            right1 = nums1[t1 + 1] if t1 < l1 else MAX
            right2 = nums2[t2 + 1] if 0 < t2 + 1 <= l2 else MAX
            if left1 > right2:
                hi = t1 if hi != t1 else t1 - 1
            elif left2 > right1:
                lo = t1 if lo != t1 else t1 + 1
            else:
                break
            t1 = (lo + hi) / 2
            t2 = (l1 + l2) / 2 - t1
        c1 = max([left1, left2])
        c2 = min([right1, right2])
        return c2 if (l1 + l2) % 2 != 0 else (c1 + c2)/2.0

a = Solution()
print(a.findMedianSortedArrays([1, 2], [3, 4]))