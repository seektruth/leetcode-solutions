class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        power_of_two = [2 ** i for i in range(31, -1, -1)]

        def find_closet_power_of_two(t):
            for x in power_of_two:
                if x <= t:
                    return x

        cons = "0b0"
        while n:
            x = find_closet_power_of_two(n)
            if x > m:
                while x:
                    cons += "0"
                    x //= 2
                break
            else:
                cons += "1"
                cons += '0' * (len(bin(n)) - len(bin(n - x)) - 1)
                m -= x
                n -= x


        return int(cons, 2)

a = Solution()
print(a.rangeBitwiseAnd(4, 5))
