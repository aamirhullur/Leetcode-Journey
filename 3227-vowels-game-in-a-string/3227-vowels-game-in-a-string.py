class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        vowels = ['a','e','i','o','u']
        cnt = 0
        
        for c in s:
            if c in vowels:
                cnt+=1
        
        if cnt == 0:
            return False
        elif cnt % 2 == 1:
            return True
        else:
            return True