class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(idx,node):
            curr = node
            for i in range(idx,len(word)):
                w = word[i]
                if w == '.':
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False 
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            return curr.word

        return dfs(0,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)