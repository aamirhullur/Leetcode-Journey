class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hmap = {i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            hmap[crs].append(pre)
    
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False

            if hmap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in hmap[crs]:
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            hmap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True