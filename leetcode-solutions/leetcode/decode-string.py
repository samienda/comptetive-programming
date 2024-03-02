class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        # prev = ""

        curr = ""
        num = 0

        for ch in s:
            # print(stack, ch, curr, num)
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append(num)
                stack.append(curr)
                curr = ""
                num = 0
            elif ch == ']':
                curr = stack.pop() + curr * stack.pop()
            else:
                curr += ch


        return curr
        