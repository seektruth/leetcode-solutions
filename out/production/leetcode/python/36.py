class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row_set = set()
            column_set = set()
            cube_set = set()
            for j in range(9):
                c1 = board[i][j]
                c2 = board[j][i]
                c3 = board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3]
                if c1 != "." and c1 in row_set:
                    return False
                if c2 != "." and c2 in column_set:
                    return False
                if c3 != "." and c3 in cube_set:
                    return False
                row_set.add(c1)
                column_set.add(c2)
                cube_set.add(c3)
        return True

a = Solution()
print a.isValidSudoku([['3', '1', '9', '7', '4', '8', '6', '5', '2'],
    ['7', '3', '2', '4', '5', '6', '1', '8', '9'],
    ['4', '2', '5', '1', '3', '9', '8', '6', '7'],
    ['5', '8', '7', '9', '6', '1', '2', '4', '3'],
    ['2', '6', '4', '3', '1', '7', '5', '9', '8'],
    ['1', '9', '8', '6', '2', '4', '3', '7', '5'],
    ['6', '5', '1', '8', '9', '3', '7', '2', '4'],
    ['9', '7', '3', '5', '8', '2', '4', '1', '6'],
    ['8', '4', '6', '2', '7', '5', '9', '3', '1']])

