class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hmap = defaultdict(list)

        for l,r in edges:
            hmap[l].append(r)
            hmap[r].append(l)
        visited = set()
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                cur = q.popleft()
                for nei in hmap[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        res = 0

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        return res