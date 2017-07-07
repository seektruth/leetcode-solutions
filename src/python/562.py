class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        m = 0
        H = [[False for j in range(len(M[0]))] for i in range(len(M))]
        V = [[False for j in range(len(M[0]))] for i in range(len(M))]
        A = [[False for j in range(len(M[0]))] for i in range(len(M))]
        D = [[False for j in range(len(M[0]))] for i in range(len(M))]


        def find_h(i, j):
            c = 1
            p = j - 1
            while p >= 0 and M[i][p] is 1 and not H[i][p]:
                H[i][p] = True
                c += 1
                p -= 1
            p = j + 1
            while p < len(M[0]) and M[i][p] is 1 and not H[i][p]:
                H[i][p] = True
                c += 1
                p += 1
            return c

        def find_v(i, j):
            c = 1
            p = i - 1
            while p >= 0 and M[p][j] is 1 and not V[p][j]:
                V[p][j] = True
                c += 1
                p -= 1
            p = i + 1
            while p < len(M) and M[p][j] is 1 and not V[p][j]:
                V[p][j] = True
                c += 1
                p += 1
            return c

        def find_d(i, j):
            c = 1
            p = i + 1
            k = j + 1
            while p < len(M) and k < len(M[0]) and M[p][k] is 1 and not D[p][k]:
                D[p][k] = True
                c += 1
                p += 1
                k += 1
            p = i - 1
            k = j - 1
            while p >= 0 and k>= 0 and M[p][k] is 1 and not D[p][k]:
                D[p][k] = True
                c += 1
                p -= 1
                k -= 1
            return c

        def find_a(i, j):
            c = 1
            p = i + 1
            k = j - 1
            while p < len(M) and k >= 0 and M[p][k] is 1 and not A[p][k]:
                A[p][k] = True
                c += 1
                p += 1
                k -= 1
            p = i - 1
            k = j + 1
            while p >= 0 and k < len(M[0]) and M[p][k] is 1 and not A[p][k]:
                A[p][k] = True
                c += 1
                p -= 1
                k += 1
            return c

        for i in range(0, len(M)):
            for j in range(0, len(M[0])):
                if M[i][j] is 1:
                    m = max((m, find_a(i, j), find_d(i, j), find_h(i, j), find_v(i, j)))
        return m

a = Solution()
print(a.longestLine([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))




