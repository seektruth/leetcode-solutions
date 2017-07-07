table = ["I", "V", "X",  "L", "C", "D", "M"]


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        consequence = "M" * (num/1000)
        i = 3
        while i > 0:
            r = (num % 10 ** i) / 10 ** (i - 1)
            if r == 9:
                consequence += table[2 * i - 2] + table[2 * i]
            elif r >= 5:
                consequence += table[2 * i - 1] + table[2 * i - 2] * (r - 5)
            elif r == 4:
                consequence += table[2 * i - 2] + table[2 * i - 1]
            else:
                consequence += table[2 * i - 2] * r
            i -= 1
        return consequence


a = Solution()
print(a.intToRoman(0))
