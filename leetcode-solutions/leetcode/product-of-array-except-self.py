class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1]
        right = [1]

        runleft = 1
        runright = 1

        for i in range(n):
            runleft *= nums[i]
            runright *= nums[n - i - 1]

            left.append(runleft)
            right.append(runright)

        left.append(1)
        right.append(1)
        right = right[::-1]


        for i in range(n):
            nums[i] = left[i] * right[i + 2]


        return nums