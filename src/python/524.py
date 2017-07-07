class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        cons = ""
        for st in d:
            partialS = s
            for char in st:
                n = partialS.find(char)
                if n < 0:
                    break
                partialS = partialS[n+1:]
            else:
                if len(st) > len(cons) or (len(st) == len(cons) and st < cons):
                    cons = st
        return st

a = Solution
a.findLongestWord(a,"abpcplea",["ale","apple","monkey","plea"])