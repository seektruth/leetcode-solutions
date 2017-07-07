class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def key(x):
            if k == 0:
                return x == k
            else:
                return x % k == 0

        sums = [x for x in nums]
        sumsNext = []
        for i in range(len(nums)):
            for j in range(len(sums) - 1):
                n = sums[j] + nums[i+j+1]
                if key(n):
                    return True
                sumsNext.append(n)
            sums = sumsNext
            sumsNext = []
        return False

a = Solution
a.checkSubarraySum(a,[23,2,6,4,7],6)