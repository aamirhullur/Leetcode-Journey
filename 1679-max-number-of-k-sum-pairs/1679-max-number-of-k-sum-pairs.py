class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        res = 0
        for n in nums:
            if k-n in hmap:
                hmap[k-n] -= 1
                if hmap[k-n] == 0:
                    hmap.pop(k-n)
                res +=1
            else:
                hmap[n] += 1
        return res