class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0

        for n in num1:
            n1 *= 10
            for d in '0123456789':
                n1 += n > d
        
        for n in num2:
            n2 *= 10
            for d in '0123456789':
                n2 += n > d
        # print(n1, n2)
        return f"{n1 * n2}"
