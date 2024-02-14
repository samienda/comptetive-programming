class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()


        for i in range(n - 1, 1, -1):
            one = nums[i - 2]
            two = nums[i - 1]
            three = nums[i]

            if (one + two  ) > three :
                return one + two + three

        return 0
        