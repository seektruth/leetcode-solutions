class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        m = 0
        l1 = 0
        l2 = len(height) - 1
        while l1 < l2:
            n = (l2 - l1)*min((height[l1], height[l2]))
            if n > m: m = n
            if height[l1] > height[l2]: l2 -= 1
            else: l1 += 1
        return m

a = Solution()
print a.maxArea([1, 4, 3, 0])