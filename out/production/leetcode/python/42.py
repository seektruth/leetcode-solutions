class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        pairs = [(i, h) for i, h in enumerate(height)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        if not pairs: return 0
        top = pairs[0]
        right = top
        leftPairs = filter(lambda x: x[0] < right[0], pairs)
        while leftPairs:
            left = leftPairs[0]
            water += left[1] * (right[0] - left[0] - 1)
            for i in range(left[0] + 1, right[0]):
                water -= height[i]
            right = left
            leftPairs = filter(lambda x: x[0] < right[0], leftPairs)
        left = top
        rightPairs = filter(lambda x: x[0] > left[0], pairs)
        while rightPairs:
            right = rightPairs[0]
            water += right[1] * (right[0] - left[0] - 1)
            for i in range(left[0] + 1, right[0]):
                water -= height[i]
            left = right
            rightPairs = filter(lambda x: x[0] > left[0], rightPairs)
        return water

a = Solution()
print(a.trap([10, 9, 0, 10]))

