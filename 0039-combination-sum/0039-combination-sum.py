class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = set()
        res = []
        def bt(currSum,arr,j):
            print(currSum, arr, res, j)
            if currSum > target:
                return 
            elif currSum == target:
                tmp.add(tuple(sorted(arr)))
                # tmp.add(tuple(arr))
                # res.append(list(arr))
            else:
                for i in range(j,len(candidates)):
                    currSum+=candidates[i]
                    arr.append(candidates[i])
                    if currSum <= target:
                        bt(currSum,arr,i)
                    currSum-=candidates[i]
                    arr.pop()

        candidates.sort()

        for i in range(len(candidates)):
            bt(candidates[i],[candidates[i]],i)
        
        return [list(i) for i in tmp]

        # return res