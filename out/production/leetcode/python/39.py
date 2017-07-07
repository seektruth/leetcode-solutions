from copy import copy
from pprint import pprint

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        cons = {}
        for t in range(target+1):
            cons[t] = []
            for n in candidates:
                if n == t:
                    cons[t].append([n])
                elif t - n in cons and cons[t - n]:
                    for c in cons[t - n]:
                        c2 = copy(c)
                        c2.append(n)
                        c2.sort()
                        if c2 not in cons[t]:
                            cons[t].append(c2)
        return cons[target]

a = Solution()
pprint(a.combinationSum([2, 3, 6, 7], 1), indent=4)
