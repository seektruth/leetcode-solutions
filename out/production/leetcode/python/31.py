class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        for i in range(1,len(nums)):
            if nums[i] >= nums[i - 1]:
                continue
            else:
                for j in range(i):
                    if nums[j] <= nums[i]:
                        continue
                    else:
                        t = nums[i]
                        nums[i] = nums[j]
                        nt = [nums[x] for x in range(j) + range(j+1, i)]
                        nt.append(t)
                        nt.sort(reverse=True)
                        if not nt: nt.append(t)
                        for k in range(i):
                            nums[k] = nt[k]
                        break
                break
        else:
            nums.sort()
            return nums
        nums.reverse()
        return nums

a = Solution()
b = a.nextPermutation([3, 2, 1])
print b








