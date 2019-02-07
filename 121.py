# 121. Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = 'inf'
        maxSoFar = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                maxSoFar = max(maxSoFar, p - minPrice)

        return maxSoFar
