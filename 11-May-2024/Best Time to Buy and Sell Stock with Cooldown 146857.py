# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def profit(idx, bought, selled):
            if idx >= len(prices):return 0

            state = (idx, bought, selled)
            if state not in memo:
                if bought:
                    memo[state] = max(
                        profit(idx + 1, bought, selled),
                        profit(idx + 1, False, True) + prices[idx],
                    )
                elif not selled:
                    memo[state] = max(
                        profit(idx + 1, bought, selled),
                        profit(idx + 1, True, selled) - prices[idx],
                    )
                else:
                    memo[state] = profit(idx + 1, bought, False)

            return memo[state]

        return profit(0, False, False)
                