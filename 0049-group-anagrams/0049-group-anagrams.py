class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        
        tmp = {}
        for i, r in enumerate(strs):
            res = [0] * 26
            for j in r:
                res[ord(j) - ord('a')] += 1
            res = ''.join(str(res))
            if res in tmp:
                tmp[res].append(r)
            else:
                tmp[res] = [r]

        return(tmp.values())
            
