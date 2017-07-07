class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set()
        i = 0
        while i < len(nums):
            num = nums[i]
            if num not in a:
                a.add(num)
                i += 1
            else:
                del nums[i]
        return len(a)

a = Solution()
a.removeDuplicates([1,1,2])
