class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        for split in "+-=":
            equation = equation.replace(split, " %s " % split)
        op = "+"
        cs = equation.split()
        index = cs.index("=")
        cs[index] = "-"
        xindex = 0
        constant = 0
        for i in range(index+1, len(cs)):
            if cs[i] == "+": cs[i] = "-"
            elif cs[i] == "-": cs[i] = "+"
        for c in cs:
            if c == "+" or c == "-":
                op = c
            elif c[-1] == "x":
                co = 1 if len(c) == 1 else int(c[:-1])
                xindex = xindex + co if op == "+" else xindex - co
            else:
                co = int(c)
                constant = constant + co if op == "+" else constant - co
        if xindex == 0 and constant != 0:
            return "No solution"
        if xindex == 0 and constant == 0:
            return "Infinite solutions"
        return "x="+ str(-1 * constant/xindex)


a = Solution()
print a.solveEquation("x+5-3+x=6+x-2")
