class Solution(object):
    def numMagicSquaresInside(self, grid):
        if len(grid)<3 and len(grid[0])<3:
            return 0

        cnt=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                sqr=[grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]

                if set(sqr)==set(range(1,10)):
                    if (sum(grid[i][j:j+3])==sum(grid[i+1][j:j+3])==sum(grid[i+2][j:j+3])==sum([grid[i][j], grid[i+1][j], grid[i+2][j]]) ==
                        sum([grid[i][j+1], grid[i+1][j+1], grid[i+2][j+1]]) == 
                        sum([grid[i][j+2], grid[i+1][j+2], grid[i+2][j+2]]) ==
                        sum([grid[i][j], grid[i+1][j+1], grid[i+2][j+2]]) ==
                        sum([grid[i][j+2], grid[i+1][j+1], grid[i+2][j]])):
                        cnt += 1

        return cnt