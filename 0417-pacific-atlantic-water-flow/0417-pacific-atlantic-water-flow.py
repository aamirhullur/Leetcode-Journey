class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ROWS = len(heights)
        # COLS = len(heights[0])

        # visited = set()
        # res = []

        # def dfs(r,c,prev):
        #     if (r == 0 or c == 0) and heights[r][c] <= prev:
        #         return True
        #     if (r == ROWS-1 or c == COLS-1) and heights[r][c] <= prev:
        #         return True
            
        #     if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or heights[r][c] > prev:
        #         return False
            
        #     visited.add((r,c))
        #     pacific = (dfs(r-1,c,heights[r][c]) or dfs(r,c-1,heights[r][c]))
        #     atlantic = (dfs(r+1,c,heights[r][c]) or dfs(r,c+1,heights[r][c]))
        #     visited.remove((r,c))

        #     return 2 if atlantic and pacific else 3
                
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if dfs(i,j,heights[i][j]) == 2:
        #             res.append([i,j])
        # return res


        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()
        res = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c,visited,prevH):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or heights[r][c] < prevH:
                return False

            visited.add((r,c))
            for dx,dy in directions:
                dfs(r+dx,c+dy,visited,heights[r][c])


        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])    
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res