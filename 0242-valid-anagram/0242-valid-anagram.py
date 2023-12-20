class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        return s == t