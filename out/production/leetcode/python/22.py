class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0: return []
        consequence = set()
        consequence.add("")
        for i in range(n):
            new_cons = set()
            for c in consequence:
                for i in range(len(c) + 1):
                    s1 = c[0:i] + "(" + c[i:]
                    for j in range(i + 1,len(s1) + 1):
                        s2 = s1[0:j] + ")" + s1[j:]
                        new_cons.add(s2)
            consequence = new_cons
        return list(consequence)

a = Solution()
print(a.generateParenthesis(4))



