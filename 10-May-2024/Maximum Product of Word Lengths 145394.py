# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        memo = [[len(word), set(word)] for word in words]

        answer = 0
        for l1, wordi in memo:
            for l2, wordj in memo:
                for ch in wordj:
                    if ch in wordi:
                        break
                else:
                    answer = max(answer, l1 * l2)

        return answer

