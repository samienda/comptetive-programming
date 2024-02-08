class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        left_right = []
        right_left = []

        runleft = 0
        runright = 0

        for i in range(n):
            runleft += nums[i]
            runright += nums[n - i - 1]

            left_right.append(runleft)
            right_left.append(runright)

        
        for i in range(n):
            if left_right[i] == right_left[n - i - 1]:
                return i

        return -1

        