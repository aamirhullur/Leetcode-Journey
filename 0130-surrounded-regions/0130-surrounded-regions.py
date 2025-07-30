class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()
        q = collections.deque()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for c in range(COLS):
            if board[0][c] == 'O' and ((0,c) not in visited):
                q.append((0,c))
                visited.add((0,c))
            if board[ROWS-1][c] == 'O' and ((ROWS-1,c) not in visited):
                q.append((ROWS-1,c))
                visited.add((ROWS-1,c))

        for r in range(ROWS):
            if board[r][0] == 'O' and ((r,0) not in visited):
                q.append((r,0))
                visited.add((r,0))
            if board[r][COLS-1] == 'O' and ((r,COLS-1) not in visited):
                q.append((r,COLS-1))
                visited.add((r,COLS-1))

        while q:
            row, col = q.popleft()
            for dx, dy in directions:
                r = row+dx
                c = col+dy
                if min(r,c) >= 0 and r < ROWS and c < COLS and (r,c) not in visited and board[r][c] == 'O':
                    q.append((r,c))
                    visited.add((r,c))


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'
        
        return board