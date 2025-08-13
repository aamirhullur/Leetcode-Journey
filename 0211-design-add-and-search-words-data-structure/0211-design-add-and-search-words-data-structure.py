class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True
        

    def search(self, word: str) -> bool:

        curr = self.root
        q = collections.deque()
        q.append([0,curr])

        while q:
            idx,node = q.popleft()

            if idx == len(word):
                if node.end:
                    return True
                continue

            ch = word[idx]

            if ch == '.':
                for child in node.children.values():
                    q.append([idx+1,child])
            else:
                if ch in node.children:
                    q.append([idx+1,node.children[ch]])
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)