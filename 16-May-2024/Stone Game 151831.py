# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        # @cache
        memo = {}
        def choose(left, right, aliceturn):
            if left > right:
                return 0

            state = (left, right, aliceturn)
            if state not in memo:
                    
                if aliceturn:
                    memo[state] = max(
                        choose(left + 1, right, False) + piles[left],
                        choose(left, right - 1, False) + piles[right]
                    )
                else:
                    memo[state] = max(
                        choose(left + 1, right, True) - piles[left],
                        choose(left, right - 1, True) - piles[right]
                    )
            return memo[state]

        return choose(0, len(piles) - 1, True)