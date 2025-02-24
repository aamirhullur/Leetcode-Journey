class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        visited = set()
        def dfs(r,c,letter):
            if letter == len(word):
                return True

            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] != word[letter]):
                return False
            
            visited.add((r,c))

            res = (dfs(r+1,c,letter+1) or dfs(r-1,c,letter+1)
                    or dfs(r,c+1,letter+1) or dfs(r,c-1,letter+1))
            
            visited.remove((r,c))

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False
    
    
                    
        
