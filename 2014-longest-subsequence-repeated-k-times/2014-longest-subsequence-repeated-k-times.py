class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        candidate = sorted([c for c, w in Counter(s).items() if w >= k],reverse=True)
        ans = ""

        q = deque(candidate)

        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for ch in candidate:
                nxt = curr+ch
                it = iter(s)
                if all(ch in it for ch in nxt *k):
                    q.append(nxt)
        return ans