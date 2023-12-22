class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new = ''
        for i,r in enumerate(s):
            if r.isalnum():
                new += r
        return new == new[::-1]