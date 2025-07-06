class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1, self.nums2 = nums1, nums2
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        value = self.nums2[index]
        self.nums2[index] += val
        self.freq2[value] -= 1

        if self.freq2[value] == 0:
            self.freq2.pop(value)
        
        value+=val
        if value in self.freq2:
            self.freq2[value] += 1
        else:
            self.freq2[value] = 1

    def count(self, tot: int) -> int:
        res = 0
        for i in self.nums1:
            if (tot - i) in self.freq2:
                res += self.freq2[tot-i]
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)