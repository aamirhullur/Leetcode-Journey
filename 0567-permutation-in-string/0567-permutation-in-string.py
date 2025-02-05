from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        hmap = {}
        for i in s1:
            if i in hmap:
                hmap[i] +=1
            else:
                hmap[i] =1
        # l = 0

        for l in range(0,len(s2)-len(s1)+1):
            hm = {}
            while l < len(s2) and s2[l] in s1:
                if s2[l] in hm:
                    hm[s2[l]] +=1
                else:
                    hm[s2[l]] = 1
                if hm == hmap:
                    return True
                elif hm[s2[l]] > hmap[s2[l]]:
                    break
                l+=1
        return False