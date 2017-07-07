import copy
import pprint


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        consenquence = [0]
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
                consenquence[0] += 1
            else:
                for i in range(n):
                    if not contradict(i):
                        forward(i)
            q.pop()

        for i in range(n):
            forward(i)
        return consenquence[0]

a = Solution()
print a.totalNQueens(8)

