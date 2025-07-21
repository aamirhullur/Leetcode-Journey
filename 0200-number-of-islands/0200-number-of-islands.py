class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def dfs(r,c,visited):

            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0" or (r,c) in visited:
                return 0
            
            visited.add((r,c))

            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)

            return 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j,visited)
                    res += 1

        return res