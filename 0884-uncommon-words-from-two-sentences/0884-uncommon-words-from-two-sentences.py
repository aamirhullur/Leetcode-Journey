class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        string = ''
        hashmap = {}
        for i in range(len(s1)):
            if s1[i] == ' ':
                hashmap[string] = hashmap.get(string, 0) + 1
                string = ''
            else:
                string = string + s1[i]
        
        hashmap[string] = hashmap.get(string, 0) + 1
        string = ''
    
        for i in range(len(s2)):
            if s2[i] == ' ':
                hashmap[string] = hashmap.get(string, 0) + 1
                string = ''
            else:
                string = string + s2[i]
        
        hashmap[string] = hashmap.get(string, 0) + 1
        string = ''
    
        result = []
        for key in hashmap:
            if hashmap[key] == 1:
                result.append(key)
        
        return result