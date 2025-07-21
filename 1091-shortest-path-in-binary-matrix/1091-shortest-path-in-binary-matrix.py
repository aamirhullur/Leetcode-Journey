class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        self.res=float('inf')
        
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        def bfs(r,c,visited):
            q = collections.deque()
            visited.add((r,c))
            cnt = 0
            q.append((r,c,visited,cnt))
            while q:
                row,col,visited,cnt = q.popleft()
                directions = [[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,1],[-1,-1],[1,-1]]
                cnt += 1
                if row == ROWS-1 and col == COLS-1:
                    self.res = min(self.res,cnt)
                for dx,dy in directions:
                    r = row+dx
                    c = col+dy
                    if min(r,c) >= 0 and r < ROWS and c < COLS and grid[r][c] == 0 and (r,c) not in visited:
                        visited.add((r,c))
                        q.append((r,c,visited,cnt))


        bfs(0,0, set())
        return self.res if self.res != float('inf') else -1