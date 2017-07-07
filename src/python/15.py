import collections


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        count = collections.Counter(nums)
        consequence = set()
        i = 0
        pre = None
        while i < len(nums) - 1:
            min_element = nums[i]
            if min_element == pre:
                i += 1
                continue
            for mid in nums[i+1:]:
                nex = 0 - min_element - mid
                if nex >= mid and nex in count:
                    require = 1
                    require += 1 if nex == min_element else 0
                    require += 1 if nex == mid else 0
                    if count[nex] >= require:
                        consequence.add((min_element, mid, nex))
            pre = min_element
            i += 1
        return [list(x) for x in list(consequence)]


a = Solution()
import pprint
pprint.pprint(a.threeSum([0,0,0]), indent=4)



