class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        d={}
        res=sorted(set(arr))
        for i in range(len(res)):
            d[res[i]]=i+1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr
