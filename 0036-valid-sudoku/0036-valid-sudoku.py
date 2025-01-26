class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        square = collections.defaultdict(set)

        for i in range(len(board)):
            col = set()
            row = set()
            # square = set()
            for j in range(len(board)):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                if board[i][j] != '.':
                    if board[i][j] in square[(i//3,j//3)]:
                        return False
                    square[(i//3,j//3)].add(board[i][j])

        return True