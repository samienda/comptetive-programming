# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def buy(idx, bought,transaction):
            if transaction == 2:return 0
            if idx >= len(prices):return 0

            state = (idx, bought,transaction)
            if state not in memo:
                if bought:
                    memo[state] = max(
                        buy(idx + 1, bought, transaction),
                        buy(idx + 1, False, transaction + 1)  + prices[idx],
                    )
                else:
                    memo[state] = max(
                        buy(idx + 1, bought, transaction),
                        buy(idx + 1, True, transaction) - prices[idx]
                        )

            return memo[state]

        return buy(0, False, 0)
