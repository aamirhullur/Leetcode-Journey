class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        total = len1+len2
        i,j = 0,0
        median = 0
        target = total//2
        cnt = 0

        
        while cnt <= target and i<len1 and j<len2:
            prevMedian = median
            if nums1[i] < nums2[j]:
                median = nums1[i]
                i+=1
            else:
                median = nums2[j]
                j+=1
            cnt += 1
        
        while cnt <= target and i < len1:
            prevMedian = median
            median = nums1[i]
            i+=1
            cnt+=1
        
        while cnt <= target and j < len2:
            prevMedian = median
            median = nums2[j]
            j+=1
            cnt+=1
        
        if total%2 == 0:
            return (prevMedian+median)/2
        else:
            return median
        
                