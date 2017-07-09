class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 1
        cache = [1 for i in range(len(s) + 1)]
        cache[-2] = 9 if s[-1] == "*" else 1
        if s[-1] == "0":
            cache[-2] = 0

        def r(n):
            first = s[n]
            second = s[n + 1]
            if first == "1":
                if second == "*":
                    cache[n] = cache[n + 1] + 9 * cache[n + 2]
                elif second == "0":
                    cache[n] = cache[n + 2]
                else:
                    cache[n] = cache[n + 1] + cache[n + 2]
            elif first == "2":
                if second == "*":
                    cache[n] = cache[n + 1] + 6 * cache[n + 2]
                elif second in "123456":
                    cache[n] = cache[n + 1] + cache[n + 2]
                elif second == "0":
                    cache[n] = cache[n + 2]
                else:
                    cache[n] = cache[n + 1]
            elif first == "0":
                cache[n] = 0
            elif first == "*":
                if second == "*":
                    cache[n] = 9 * cache[n + 1] + 15 * cache[n + 2]
                elif second == "0":
                    cache[n] = 2 * cache[n + 2]
                elif second in "789":
                    cache[n] = 9 * cache[n + 1] + cache[n + 2]
                elif second in "123456":
                    cache[n] = 9 * cache[n + 1] + 2 * cache[n + 2]
            else:
                cache[n] = cache[n+1]
            cache[n] = cache[n] % (10 ** 9 + 7)

        for i in range(len(s) - 2, -1, -1):
            r(i)
        return cache[0]

a = Solution()
print a.numDecodings("*10*1")



