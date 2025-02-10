class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                stack.pop()
        
        if stack:
            return "".join(stack)
        else:
            return ""