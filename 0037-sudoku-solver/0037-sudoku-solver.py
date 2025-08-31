class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n = len(board)

        ROWS, COLS = len(board),len(board[0])

        rowMap, colMap, squareMap = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                
                v = int(board[r][c])

                rowMap[r].add(v)
                colMap[c].add(v)
                squareMap[((r//3) * 3 + c//3)].add(v)
        
        def is_valid(r,c,v):
            box = (r//3) * 3 + c//3
            return v not in rowMap[r] and v not in colMap[c] and v not in squareMap[box]

        def bt(r,c):
            if r == n-1 and c == n:
                return True
            elif c == n:
                c = 0
                r+=1
            
            if board[r][c] != '.':
                return bt(r,c+1)
            
            box = (r//3) * 3 + c//3

            for v in range(1,n+1):
                if not is_valid(r,c,v):
                    continue

                board[r][c] = str(v)
                rowMap[r].add(v)
                colMap[c].add(v)
                squareMap[box].add(v)

                if bt(r,c+1):
                    return True
                
                board[r][c] = '.'
                rowMap[r].remove(v)
                colMap[c].remove(v)
                squareMap[box].remove(v)
            
            return False
        

        bt(0,0)