class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ps = []
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i+1] == '*':
                ps.append(p[i:i+2])
                i += 2
            else:
                ps.append(p[i])
                i += 1



