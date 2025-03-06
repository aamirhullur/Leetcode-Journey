class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # n = len(grid) * len(grid[0])
        # hmap = [0] * n
        # res = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] in hmap:
        #             res.append(grid[i][j])
        #         else:
        #             # hmap[grid[i,j]]
        #             hmap[grid[i][j]-1] = grid[i][j]
        
        # for i in range(len(hmap)):
        #     if hmap[i] == 0:
        #         res.append(i+1)
        # return res


        n = len(grid) * len(grid[0])
        hmap = set()
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in hmap:
                    res.append(grid[i][j])
                else:
                    # hmap[grid[i,j]]
                    hmap.add(grid[i][j])
        
        for i in range(1,n+1):
            if i not in hmap:
                res.append(i)
        return res
