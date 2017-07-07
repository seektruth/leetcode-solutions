from copy import copy
from pprint import pprint

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        cons = {}
        nums = list(range(1, 10))
        for t in range(n+1):
            cons[t] = []
            for i in nums:
                if i == t:
                    cons[t].append([i])
                elif t - i in cons and cons[t - i]:
                    for c in cons[t - i]:
                        if len(c) < k and i not in c:
                            c2 = copy(c)
                            c2.append(i)
                            c2.sort()
                            if c2 not in cons[t]:
                                cons[t].append(c2)
        return filter(lambda x: len(x) == k, cons[n])

a = Solution()
print(a.combinationSum3(2, 0))
