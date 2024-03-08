class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        bits = list(s)
        bits.sort()
      
        idx = bits.index('1')

        bits[0], bits[idx] = bits[idx], bits[0]

        return "".join(reversed(bits)) 
        