class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,currStack):

            if i == len(nums): 
                res.append(list(currStack))
                return
                
            currStack.append(nums[i])
            dfs(i+1,currStack)

            currStack.pop()
            dfs(i+1,currStack)


        dfs(0,[])

        return res