class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        oper = 0

        for i in range(n - 2, -1, -1):
            num = nums[i + 1]
            k = math.ceil(nums[i] / num)
            oper += k - 1
            nums[i] = nums[i] // k

        return oper  



        