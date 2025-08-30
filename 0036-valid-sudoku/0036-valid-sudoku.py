class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, squareMap = defaultdict(set), defaultdict(set), defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                # print(board[r][c])
                # print(rowMap)
                # print(colMap)
                # print(squareMap)
                if board[r][c] != '.':
                    if board[r][c] in rowMap[r] or board[r][c] in colMap[c] or board[r][c] in squareMap[(r//3,c//3)]:
                        return False

                    rowMap[r].add(board[r][c])
                    colMap[c].add(board[r][c])
                    squareMap[(r//3,c//3)].add(board[r][c])

        return True