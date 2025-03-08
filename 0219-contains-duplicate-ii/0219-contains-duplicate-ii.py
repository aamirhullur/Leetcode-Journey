class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        hset = set()
        for r in range(len(nums)):
            if nums[r] in hset:
                return True
            hset.add(nums[r])

            if r-l == k:
                hset.remove(nums[l])
                l+=1
        return False
