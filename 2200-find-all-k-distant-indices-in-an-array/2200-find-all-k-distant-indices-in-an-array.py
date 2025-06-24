class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = 0
        res = set()
        for r in range(len(nums)):
            if r-l > k:
                l+=1
            while nums[r] == key and abs(r-l) <= k and l < len(nums):
                res.add(l)
                l+=1

        return list(res)