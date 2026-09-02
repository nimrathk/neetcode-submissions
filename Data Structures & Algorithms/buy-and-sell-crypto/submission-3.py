class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0

        while r < len(prices) and l < r:
            maxP = max(maxP, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1

        return maxP