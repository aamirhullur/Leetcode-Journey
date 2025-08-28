class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        for x,y in adjacentPairs:
            adjMap[x].append(y)
            adjMap[y].append(x)
        
        # {
        #     1:2
        #     2:1,3
        #     3:2,4
        #     4:3
        # }

        root = None
        for num in adjMap:
            if len(adjMap[num]) == 1:
                root = num
                break
        
        arr = []

        q = collections.deque()
        q.append(root)
        visited = set([root])

        while q and len(arr) < len(adjacentPairs) + 1:
            curr = q.popleft()
            arr.append(curr)
            for nei in adjMap[curr]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return arr
        
        