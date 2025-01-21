class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        pref1 = [0] * m
        pref2 = [0] * m

        pref1[0] = grid[0][0]
        pref2[0] = grid[1][0]

        for i in range(1, m):
            pref1[i] = pref1[i - 1] + grid[0][i]
            pref2[i] = pref2[i - 1] + grid[1][i]

        result = float('inf')
        for i in range(m):
            top = 0 if i == m - 1 else pref1[m - 1] - pref1[i]
            bottom = 0 if i == 0 else pref2[i - 1]
            result = min(result, max(top, bottom))

        return result