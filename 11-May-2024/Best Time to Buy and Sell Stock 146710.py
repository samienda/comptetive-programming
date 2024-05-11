# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        mini = prices[0]
        ans = 0
        for price in prices[1:]:

            if price > mini:
                ans = max(ans, price - mini)
            else:
                mini = price

        return ans
