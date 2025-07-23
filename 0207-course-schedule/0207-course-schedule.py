class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hmap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hmap[crs].append(pre)
        
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            
            if hmap[crs] == []:
                return True

            visit.add(crs)
            for pre in hmap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            hmap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

