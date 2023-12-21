class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = {}

        for i,r in enumerate(strs):
            r_sorted = ''.join(sorted(r))
            if r_sorted in temp:
                temp[r_sorted].append(r)
            else:
                temp[r_sorted] = [r]
        sorted_lists = [sorted(value) for value in temp.values()]
        result = sorted(sorted_lists, key=len)
        return(result)