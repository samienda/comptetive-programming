# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}
        def transaction(idx, bought):
            if idx >= len(prices):return 0

            state = (idx, bought)
            if state not in memo:
                if bought:
                    memo[state] = max(
                        transaction(idx + 1, bought), 
                        transaction(idx + 1, False) + prices[idx] -fee
                        )
                else:
                    memo[state] = max(
                        transaction(idx + 1, bought), 
                        transaction(idx + 1, True) - prices[idx]
                        )

            return memo[state]

        return transaction(0, False) 