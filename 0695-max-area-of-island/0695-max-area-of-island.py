class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        def dfs(r,c):

            if min(r,c) < 0 or r==ROWS or c == COLS or grid[r][c] == 0:
                return 0

            grid[r][c]=0
            cnt = 1
            
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dx,dy in directions:
                cnt += dfs(r+dx,c+dy)
            
            return cnt

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        
        return res
