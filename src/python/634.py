class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = [0, 0, 1]
        for i in range(3, n + 1):
            cache.append(((i - 1) * (cache[i-1]+cache[i-2])) % (10 ** 9 + 7))
        return cache[n]

a = Solution()
print a.findDerangement(4)
