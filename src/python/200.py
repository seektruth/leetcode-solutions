class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    lands.add((i, j))

        def neiboors(i, j):
            return [(i-1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        def compact(i, j):
            for a, b in neiboors(i, j):
                if (a, b) in lands:
                    lands.remove((a, b))
                    compact(a, b)

        island = 0
        while len(lands) > 0:
            island += 1
            i, j = lands.pop()
            compact(i, j)
        return island

a = Solution()
g = ["111", "010", "111"]
print(a.numIslands(g))