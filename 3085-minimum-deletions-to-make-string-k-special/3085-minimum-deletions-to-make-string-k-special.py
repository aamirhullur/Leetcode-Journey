class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = {}

        for i in range(len(word)):
            if word[i] in freq:
                freq[word[i]] += 1
            else:
                freq[word[i]] = 1

        res = len(word)

        freq_list = list(freq.values())
        for val in range(len(freq_list)):
            deleted = 0 
            for j in range(len(freq_list)):
                if freq_list[j] < freq_list[val]:
                    deleted += freq_list[j]
                elif freq_list[j] > freq_list[val]+k:
                    deleted += freq_list[j] - (freq_list[val]+k)

            res = min(res,deleted)

        return res
            