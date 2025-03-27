class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())
        # if hmap1.keys() == hmap2.keys():
        #     if hmap1 == hmap2 or sorted(hmap1.values()) == sorted(hmap2.values()):
        #         return True
        #     else:
        #         return False
        # else:
        #     return False