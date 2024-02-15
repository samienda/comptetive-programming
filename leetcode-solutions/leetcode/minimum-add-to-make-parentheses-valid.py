class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        count = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    count += 1
                else:
                    stack.pop()

        return count + len(stack)

        
        