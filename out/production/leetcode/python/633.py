import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i ** 2 < (c / 2+1):
            r = c - i ** 2
            if math.sqrt(r) == int(math.sqrt(r)):
                return True
            i += 1
        return False

a = Solution()
print a.judgeSquareSum(1)

