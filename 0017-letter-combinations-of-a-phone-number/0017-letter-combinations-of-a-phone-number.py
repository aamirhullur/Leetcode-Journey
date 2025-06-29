class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        res = []

        if len(digits) == 0:
            return res
            
        def bt(i,s):
            if len(s) == len(digits):
                res.append(s)
                return
            
            for j in range(i,len(digits)):
                for k in digit_to_letter[digits[j]]:
                    s += k
                    bt(j+1,s)
                    s = s[:-1]

        bt(0,"")
        return res