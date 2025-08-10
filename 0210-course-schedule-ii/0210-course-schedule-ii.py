class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = {i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            hmap[crs].append(pre)


        visited, completed = set(), set()
        res = []
        def dfs(crs):
            if crs in visited:
                return False
            if crs in completed:
                return True

            visited.add(crs)
            for nei in hmap[crs]:
                if not dfs(nei):
                    return False
            visited.remove(crs)
            completed.add(crs)
            res.append(crs)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
        return res