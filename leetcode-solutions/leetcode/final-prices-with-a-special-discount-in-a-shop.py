class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        ans = []

        for j in range(n):

            while stack and prices[stack[-1]] >= prices[j]:
                i =  stack.pop()
                prices[i] -= prices[j]

            stack.append(j)

        return prices
        