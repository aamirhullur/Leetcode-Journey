class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # minPrice , maxProfit = float('inf'), 0
        # for price in prices:
        #     if price < minPrice:
        #         minPrice = price
        #     elif price - minPrice > maxProfit:
        #         maxProfit = price - minPrice
        # return maxProfit
        l,r = 0,1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] 
                maxProfit = max(profit,maxProfit)
            else:
                l = r
            r += 1
        return maxProfit
