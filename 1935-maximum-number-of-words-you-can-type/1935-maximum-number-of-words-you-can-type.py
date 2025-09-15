class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        hset = set()
        for i in brokenLetters:
            hset.add(ord(i))

        flip = False

        for char in text:
            if char == ' ':
                if not flip:
                    res+=1
                flip = False
            else:
                if ord(char) in hset:
                    flip = True
        
        if not flip:
            res += 1

        return res
                