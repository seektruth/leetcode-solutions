class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        l = len(str(x))
        c = 0
        t = x
        for i in range(l-1, -1, -1):
            t, y = divmod(t, 10)
            c += y * int(pow(10, i))
        return c == x

a = Solution()
print a.isPalindrome(33333)

