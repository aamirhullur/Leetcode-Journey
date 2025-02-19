class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp = set()

        def bt(currSum,arr,j):
            # print(currSum, arr, tmp, j)
            if currSum > target:
                return 
            elif currSum == target:
                tmp.add(tuple(sorted(arr)))
            else:
                for i in range(j,len(candidates)):
                    currSum+=candidates[i]
                    arr.append(candidates[i])
                    if currSum <= target:
                        bt(currSum,arr,i)
                    currSum-=candidates[i]
                    arr.pop()

        candidates.sort()

        for i in candidates:
            bt(i,[i],0)
        
        return [list(i) for i in tmp]