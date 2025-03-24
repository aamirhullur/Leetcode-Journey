class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxCurr = 0
        curr = 0
        for n in range(len(gain)):
            curr += gain[n]
            maxCurr = max(maxCurr,curr)

        return maxCurr