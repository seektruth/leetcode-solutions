class Solution(object):
    def findMin(self, nums, lo=0, hi=-1):
        if hi == -1: hi = len(nums) - 1
        while True:
            if hi == lo or nums[hi-1] > nums[hi]:
                return nums[hi]
            if hi == lo + 1:
                return min(nums[lo], nums[hi])
            else:
                mid = lo + (hi - lo) / 2
                if nums[mid] < nums[hi]:
                    hi = mid
                elif nums[mid] > nums[hi]:
                    lo = mid
                elif nums[mid] == nums[hi]:
                    return min(self.findMin(nums,lo,mid),self.findMin(nums,mid,hi))




a = Solution()
print(a.findMin([3,3,1,3,3,3,3,3,3,3,3,3,3,3,3,3]))
