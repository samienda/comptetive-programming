# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        bits = [0 for i in range(maximumBit)]
        memo = {}
        for i, num in enumerate(nums):
            
            for j in range(num.bit_length()):
                if num & 1 << (j):
                    bits[j] += 1 if not bits[j] else -1
            
            memo[i] = bits[:]


        answer = []
        for _ in memo:
            curr = 0
            for i, b in enumerate(memo[_]):
                if not b:
                    curr += 2**i
            answer.append(curr)


        return answer[::-1]