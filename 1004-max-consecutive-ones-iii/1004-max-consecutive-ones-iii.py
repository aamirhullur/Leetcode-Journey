class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        hmap = defaultdict(int)
        for r in range(len(nums)):
            hmap[nums[r]] += 1
            while hmap[0] > k:
                hmap[nums[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res
