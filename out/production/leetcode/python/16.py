class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr > target:
                    k -= 1
                elif curr < target:
                    j += 1
                else:
                    return target
                closest = curr if abs(target - curr) < abs(target - closest) else closest
        return closest

a = Solution()
print a.threeSumClosest([-1, 2, 1, -4], 1)
