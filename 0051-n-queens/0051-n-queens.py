class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."]*n for _ in range(n)]

        def bt(r):
            if r == n:
                res.append(["".join(board[i]) for i in range(len(board))])
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                bt(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        bt(0)
        return res
            