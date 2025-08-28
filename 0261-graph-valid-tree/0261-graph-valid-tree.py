class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adjMap = defaultdict(list)

        for l,r in edges:
            adjMap[l].append(r)
            adjMap[r].append(l)
        
        visited = set()

        def dfs(node,prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adjMap[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False
            visited.remove(node)
            return True

        return dfs(0,-1)
