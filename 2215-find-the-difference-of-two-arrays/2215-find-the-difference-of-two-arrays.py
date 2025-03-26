class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hset1 = set(nums1)
        hset2 = set(nums2)

        answer = [[],[]]
        for i in hset2:
            if i not in hset1:
                answer[1].append(i)
        
        for i in hset1:
            if i not in hset2:
                answer[0].append(i)
        
        return answer
