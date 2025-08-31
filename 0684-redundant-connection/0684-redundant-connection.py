class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adjMap = defaultdict(list)
        n = len(edges)

        def dfs(node,prev):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adjMap[node]:
                if nei == prev:
                    continue
                if dfs(nei,node):
                    return True

            return False

        for l,r in edges:
            adjMap[l].append(r)
            adjMap[r].append(l)
            visited = set()
            if dfs(l,-1):
                return [l,r]

        return []
