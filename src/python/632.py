class Solution(object):
    def smallestRange(self, A):
        A = [row[::-1] for row in A]

        ans = -1e9, 1e9
        for left in sorted(reduce(set.union, map(set, A))):
            right = -1e9
            for B in A:
                while B and B[-1] < left:
                    B.pop()
                if not B:
                    return ans
                right = max(right, B[-1])
            if right - left < ans[1] - ans[0]:
                ans = left, right
        return ans

a = Solution()
print a.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])