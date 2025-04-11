class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low, high + 1):
            i_str = str(i)
            if len(i_str) % 2 == 0:
                mid = len(i_str) // 2
                left_sum = sum(int(i_str[j]) for j in range(0, mid))
                right_sum = sum(int(i_str[j]) for j in range(mid, len(i_str)))
                if left_sum == right_sum:
                    res += 1
        return res