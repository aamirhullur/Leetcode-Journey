class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        freq = sorted(freq.items(), reverse=True)
        for k,v in freq:
            if k == v:
                return k
        return -1
            