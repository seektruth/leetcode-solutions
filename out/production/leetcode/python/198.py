class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {0: 0}

        def r(nums):
            l = len(nums)
            if l is 1:
                cache[l] = nums[0]
            if l is 2:
                cache[l] = max(nums)
            else:
                cache[l] = max([self.r(nums[1:]), nums[0] + self.r(nums[2:])])
            return cache[l]
        r(nums)
        return cache[len(nums)]