class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if sum(candidates) < target:
            return []
        elif sum(candidates) == target:
            return [candidates]

        res = []
        def bt(j,arr,currSum):
            if currSum == target:
                # res.add(tuple(arr))
                res.append(list(arr))
                return
                
            if j >= len(candidates) or currSum > target:
                return
            
            currSum += candidates[j]
            arr.append(candidates[j])
            bt(j+1,arr,currSum)

            arr.pop()
            currSum -= candidates[j]
            while j+1 < len(candidates) and candidates[j+1] == candidates[j]:
                j+=1
            bt(j+1,arr,currSum)

        candidates.sort()
        bt(0,[],0)

        return res
