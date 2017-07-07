import pprint


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        stack = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == ".":
                    stack.append((i, j))

        def r():
            if stack:
                i, j = stack.pop()
                can_fill = {"1","2","3","4","5","6","7","8","9"}
                for n in range(9):
                    if board[i][n] in can_fill: can_fill.remove(board[i][n])
                    if board[n][j] in can_fill: can_fill.remove(board[n][j])
                    m = i/3 * 3 + j / 3
                    if board[m / 3 * 3 + n / 3][(m % 3)*3 + n % 3] in can_fill:
                        can_fill.remove(board[m / 3 * 3 + n / 3][(m % 3)*3 + n % 3])
                if len(can_fill) == 0:
                    stack.append((i, j))
                    return "contradict"
                else:
                    for c in can_fill:
                        board[i][j] = c
                        state = r()
                        if state == "contradict":
                            board[i][j] = "."
                            continue
                        elif state == "OK":
                            return "OK"
                    stack.append((i, j))
                    return "contradict"
            else:
                return "OK"
        r()

a = Solution()
sample = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
sample = [list(x) for x in sample]
a.solveSudoku(sample)
pprint.pprint(sample,indent=4)




