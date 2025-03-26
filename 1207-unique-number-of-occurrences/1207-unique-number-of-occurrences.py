class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = defaultdict(int)
        
        for i in arr:
            hmap[i]+=1
        
        
        return (len(set(hmap.values())) == len(hmap.keys()))
