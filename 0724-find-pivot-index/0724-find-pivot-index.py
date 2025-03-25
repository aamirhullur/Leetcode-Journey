class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        curr = 0 
        for p in range(len(nums)):
            curr += nums[p]
            prefix[p+1] = curr
        print(prefix)

        for i in range(len(nums)):
            if prefix[i] == (prefix[-1] - prefix[i+1]):
                return i
        return -1