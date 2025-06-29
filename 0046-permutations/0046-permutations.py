class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(arr,currArr):
            if len(arr) == len(nums):
                res.append(list(arr))
                return
            
            for j in range(len(nums)):
                if j in currArr:
                    continue
                arr.append(nums[j])
                currArr.append(j)
                dfs(arr,currArr)
                arr.pop()
                currArr.pop()

        dfs([],[])
        return(res)