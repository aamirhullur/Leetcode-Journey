class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        currSum = 0
        res = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum - k in hmap:
                res += hmap[currSum-k]
            hmap[currSum] += 1
        return res
