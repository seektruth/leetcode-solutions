class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        cons = 0
        while dividend >= divisor:
            substractor = divisor
            multiply = 1
            while dividend >= substractor:
                dividend -= substractor
                cons += multiply
                substractor <<= 1
                multiply <<= 1
        cons = cons if positive else -cons
        if cons < -2147483648 or cons > 2147483647:
            cons = 2147483647
        return cons

a = Solution()
print(a.divide(10000, -1))

