class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        col_map = defaultdict(list)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                col_map[col].append(grid[row][col])

        columns = [tuple(col_map[col]) for col in range(len(grid))]

        res = 0
        for i in grid:
            # if i in col_map.values():
                # res+=1
            row_tuple = tuple(i)
            res += columns.count(row_tuple)
        
        return res
