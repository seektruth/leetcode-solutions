from copy import copy
from pprint import pprint
import collections

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        cons = {}
        counter = collections.Counter(candidates)
        for t in range(target + 1):
            cons[t] = []
            for n in candidates:
                if n == t and [n] not in cons[t]:
                    cons[t].append([n])
                elif t - n in cons and cons[t - n]:
                    for c in cons[t - n]:
                        if c.count(n) < counter[n]:
                            c2 = copy(c)
                            c2.append(n)
                            c2.sort()
                            if c2 not in cons[t]:
                                cons[t].append(c2)
        return cons[target]

a = Solution()
pprint(a.combinationSum2([10, 1, 2, 7, 6, 1, 5], 3), indent=4)