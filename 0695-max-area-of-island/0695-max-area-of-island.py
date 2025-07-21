class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        # def dfs(r,c):

        #     if min(r,c) < 0 or r==ROWS or c == COLS or grid[r][c] == 0:
        #         return 0

        #     grid[r][c]=0
        #     cnt = 1
            
        #     directions = [[1,0],[-1,0],[0,1],[0,-1]]

        #     for dx,dy in directions:
        #         cnt += dfs(r+dx,c+dy)
            
        #     return cnt

        visited = set()
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            cnt = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dx,dy in directions:
                    r = row+dx
                    c = col+dy
                    if min(r,c) >= 0 and r < ROWS and c < COLS and grid[r][c] == 1 and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
                        cnt+=1
                        
            return cnt

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # res = max(res,dfs(i,j))
                    res = max(res,bfs(i,j))
        
        return res
