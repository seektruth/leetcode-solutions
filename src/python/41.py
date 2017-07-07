class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def swap(i, j):
            nums[i] = nums[i] + nums[j]
            nums[j] = nums[i] - nums[j]
            nums[i] = nums[i] - nums[j]

        def check(pos):
            if 0 < nums[pos] < len(nums) + 1 and pos + 1 != nums[pos] and nums[nums[pos] - 1] != nums[pos]:
                swap(pos, nums[pos] - 1)
                check(pos)
        for i, num in enumerate(nums):
            check(i)
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1

a = Solution()
print(a.firstMissingPositive([2,2]))

