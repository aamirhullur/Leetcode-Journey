class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = set(nums)
        streak = 0
        for i in hmap:
            if (i-1) not in hmap:
                curr =1
                while (i+curr) in hmap:
                    curr+=1
                streak = max(curr,streak)
        return streak