import bisect


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        (left, right) = (-1, -1) if left>=len(nums) or nums[left] != target else (left, right - 1)
        return [left, right]

a = Solution()
print a.searchRange([2, 2], 7)