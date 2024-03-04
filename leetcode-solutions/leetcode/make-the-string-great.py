class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        isinvalid = False

        for ch in s:

            if stack and stack[-1] == ch.swapcase():

                stack.pop()

                continue

            stack.append(ch)


        return "".join(stack)