class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        def bt(currArr,visited):
            # print(currArr,visited)
            if len(currArr) == len(nums):
                res.add(tuple(currArr))
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                currArr.append(nums[i])
                visited.add(i)

                bt(currArr,visited)
                currArr.pop()
                visited.discard(i)

        bt([], set())
        return [list(x) for x in res]