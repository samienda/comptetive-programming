# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = {}
        def pick(summ, last):

            if summ >= amount:
                return 1 if summ == amount else 0

            
            state = (summ, last)
            if state not in memo:
                found = 0
                for coin in coins:
                    if last <= coin:
                        found = found +  pick(summ + coin, coin)

                memo[state] = found
            return memo[state] 

        return pick(0, 0)