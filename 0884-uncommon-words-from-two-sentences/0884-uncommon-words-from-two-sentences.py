class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
#         string = ''
#         hashmap = {}
#         for i in range(len(s1)):
#             if s1[i] == ' ':
#                 hashmap[string] = hashmap.get(string, 0) + 1
#                 string = ''
#             else:
#                 string = string + s1[i]
        
#         hashmap[string] = hashmap.get(string, 0) + 1
#         string = ''
    
#         for i in range(len(s2)):
#             if s2[i] == ' ':
#                 hashmap[string] = hashmap.get(string, 0) + 1
#                 string = ''
#             else:
#                 string = string + s2[i]
        
#         hashmap[string] = hashmap.get(string, 0) + 1
#         string = ''
    
#         result = []
#         for key in hashmap:
#             if hashmap[key] == 1:
#                 result.append(key)
        
#         return result

        words = s1.split() + s2.split()
        
        # Count the frequency of each word
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # Collect words that appear exactly once
        result = [word for word in word_count if word_count[word] == 1]
        
        return result