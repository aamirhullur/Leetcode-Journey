class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        res = ''

        for s in strs:
            res += '#_#' + str(len(s)) + '#_#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        l = 0
        res = []
        n = len(s)
        # print(s)
        SEP = '#_#'
        while l < n:
            l += len(SEP)
            r = l
            while s[r:r+3] != SEP:
                r+=1
            # print(l,r)
            # print(s[l:r])
            length = s[l:r]
            length = int(length)
            r+=len(SEP)
            l=r
            r += length
            res.append(s[l:r])
            l = r
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))