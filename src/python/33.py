class Solution(object):
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        mid = (lo + hi) / 2
        while lo < hi:
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid

a = Solution()
a.search([3, 4, 5, -5, -4, -3, -2, -1], -5)