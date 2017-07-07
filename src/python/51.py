import copy
import pprint

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        consenquence = []
        q = []

        def contradict(column):
            row = len(q)
            for i, j in enumerate(q):
                if column == j or row - i == column - j or j - column == row - i:
                    return True
            return False

        def forward(i):
            q.append(i)
            if len(q) == n:
                ns = []
                for i in range(n):
                    ns.append("." * q[i] + "Q" + "." * (n - q[i] - 1))
                consenquence.append(ns)
            else:
                for i in range(n):
                    if not contradict(i):
                        forward(i)
            q.pop()

        for i in range(n):
            forward(i)
        return consenquence

a = Solution()
for t in a.solveNQueens(2):
    print t



