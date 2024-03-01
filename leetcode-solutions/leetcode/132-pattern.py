class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        k = float('-inf')

        for num in reversed(nums):
            if num < k:
                return True

            while stack and num > stack[-1]:
                k = stack.pop()

            stack.append(num)

        return False
        