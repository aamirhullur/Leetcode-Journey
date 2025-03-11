class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def atleast(k):

            hmap = defaultdict(int)
            con = 0
            l = 0
            res=0
            for r in range(len(word)):
                if word[r] in 'aeiou':
                    hmap[word[r]] += 1
                else:
                    con+=1
                while len(hmap) == 5 and con >= k:
                    res+=(len(word)-r)
                    if word[l] in 'aeiou':
                        hmap[word[l]] -= 1
                        if hmap[word[l]] == 0:
                            hmap.pop(word[l])
                    else:
                        con-=1

                    l+=1
            return res

        return atleast(k) - atleast(k+1)