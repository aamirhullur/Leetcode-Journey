class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        rotten_cnt = 0
        oranges = 0
        q = collections.deque()
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited.add((i,j))
                    oranges += 1
                if grid[i][j] == 1:
                    oranges += 1
        
        while q:
            r,c,t = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            res = max(t,res)
            grid[r][c] = 2
            rotten_cnt += 1
            for dx,dy in directions:
                nr = r+dx
                nc = c+dy
                if min(nr,nc)>=0 and nr<ROWS and nc<COLS and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    q.append((nr,nc,t+1))
                    visited.add((nr,nc))

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == 1:
        #             return -1

        if rotten_cnt == oranges:
            return res
        else:
            return -1