class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        def neighbors(r, c):
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if (dr or dc) and 0 <= r + dr < len(board) and 0 <= c + dc < len(board[0]):
                        yield r + dr, c + dc

        x, y = click
        cmd = board[x][y]
        if cmd == "M":
            board[x][y] = "X"
        elif cmd == "E":
            mines_adj = sum(board[nr][nc] in 'MX' for nr, nc in neighbors(x, y) )
            if mines_adj == 0:
                board[x][y] = "B"
                for p, k in neighbors(x, y):
                    self.updateBoard(board, [p, k])
            else:
                board[x][y] = str(mines_adj)

        return board


a = Solution()
b = a.updateBoard([["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], [3, 0])
print(b)