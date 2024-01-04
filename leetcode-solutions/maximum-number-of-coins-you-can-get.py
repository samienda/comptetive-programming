class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        k = 0
        you = 0
        while len(piles) > k:
            piles.pop()
            you += piles.pop()
            k += 1

        return you
            
        