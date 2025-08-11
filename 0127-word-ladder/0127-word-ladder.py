class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hmap = collections.defaultdict(list)

        wordList.append(beginWord)
        for word in wordList:
            for w in range(len(word)):
                pattern = word[:w] + '*' + word[w+1:]
                hmap[pattern].append(word)
        q = collections.deque()
        q.append((beginWord,1))
        res = 1 
        visited = set([beginWord])
        while q:
            currWord, cnt = q.popleft()
            if currWord == endWord:
                return cnt
            for j in range(len(currWord)):
                pattern = currWord[:j] + '*' + currWord[j+1:]
                for nei in hmap[pattern]:
                    if nei not in visited:
                        q.append((nei,cnt+1))
                        visited.add(nei)
        return 0