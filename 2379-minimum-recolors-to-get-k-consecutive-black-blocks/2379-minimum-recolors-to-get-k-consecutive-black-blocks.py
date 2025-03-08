class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        res = k
        l,r = 0,0
        cnt = 0
        while r< len(blocks):
            if blocks[r] == 'W':
                cnt+=1
            
            if r - l + 1 == k:
                print([l,r,cnt,res])
                res = min(res,cnt)
                if blocks[l] == 'W':
                    cnt-=1
                l+=1
            r+=1
        return res
