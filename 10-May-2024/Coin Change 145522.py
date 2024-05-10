# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort(reverse=True)
    
        memo = {}
        answer = float('inf')
        def pick(summ, curr):
            nonlocal answer
            if summ == amount:
                answer = min(answer, len(curr))
                return 

            if summ > amount:
                return

            if summ in memo and memo[summ] <= len(curr):
                return

            memo[summ] = len(curr)
            for coin in coins:

                pick(summ + coin, curr + [coin])

        pick(0, [])
        return answer if answer != float('inf') else -1
