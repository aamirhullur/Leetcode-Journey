class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = defaultdict(int)

        for i in range(0,len(numbers)):
            if target-numbers[i] in hashmap:
                return [hashmap[target-numbers[i]]+1 ,i+1]
            else:
                hashmap[numbers[i]] = i
        
