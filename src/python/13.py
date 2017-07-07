table = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        consequence = 0
        while i < len(s):
            c = s[i]
            n = s[i + 1] if i + 1 < len(s) else "I"
            delta = table[c] if table[c] >= table[n] else -1 * table[c]
            consequence += delta
            i += 1
        return consequence

a = Solution()
print(a.romanToInt("C"))
