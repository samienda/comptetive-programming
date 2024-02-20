class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        prefix = [0] * n
        total = 0
        opening = []

        for i in range(n):
            if s[i] == ')':
                left = stack.pop()
                if i - 1 == left:
                    prefix[i] = 1
                    prefix[left] = 1
                    opening.append(left)
                else:
                    prefix[i] = (1/2)
                    prefix[left] = (2)
            else:
                stack.append(i)

        # print(prefix)

        for i in range(1, n):
            prefix[i] *= prefix[i - 1]
        
        # print(prefix)
        # print(opening)
        for i in opening:
            total += prefix[i]
        # print(total)


        return int(total)
        