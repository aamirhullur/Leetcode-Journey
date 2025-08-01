class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            crsMap[crs].append(pre)

        completed, visited = set(), set()

        res = []

        def dfs(crs):
            if crs in visited:
                return False
            if crs in completed:
                return True
            
            visited.add(crs)
            for p in crsMap[crs]:
                if dfs(p) == False:
                    return False
            visited.remove(crs)
            completed.add(crs)
            
            res.append(crs)
            return True

        for n in range(numCourses):
            if dfs(n) == False:
                return []
        return res
        