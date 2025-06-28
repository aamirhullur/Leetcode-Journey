class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i,currStack):
            if i >= len(nums):
                res.append(list(currStack))
                return
                
            currStack.append(nums[i])
            dfs(i+1,currStack)

            currStack.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i+1,currStack)

        nums.sort()
        dfs(0,[])
        return res