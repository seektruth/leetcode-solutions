from functools import reduce

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache = []
        digits = [int(x) for x in str(n)]
        while True:
            newn = reduce(lambda x, y: int(x + y*y), digits, 0)
            digits = [int(x) for x in str(newn)]
            if newn is 1:
                return True
            elif newn in cache:
                return False
            cache.append(newn)

a = Solution()
a.isHappy(7)