class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add_word(self,word):
        curr = self

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.add_word(w)

        row, col = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r,c,node,word):
            if (
                r<0 or c<0 or
                r >= row or c >= col or
                board[r][c] not in node.children or (r,c) in visited                
                ):
                return 
        
            visited.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visited.remove((r,c))

        
        for r in range(row):
            for c in range(col):
                dfs(r,c,root,"")
        return list(res)