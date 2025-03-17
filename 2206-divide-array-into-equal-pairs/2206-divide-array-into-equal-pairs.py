class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        hmap = Counter(nums)

        for i in hmap.values():
            if i % 2 != 0:
                return False
        return True