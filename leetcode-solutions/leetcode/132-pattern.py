class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        lastmid = float('-inf')

        for num in reversed(nums):
            if num < lastmid:
                return True
            # print(stack)

            while stack and stack[-1] < num:
                lastmid = stack.pop()

            stack.append(num)

        return False
        