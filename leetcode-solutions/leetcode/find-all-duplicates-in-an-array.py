class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = [0] * n

        ans = set()
        for num in nums:
            check[num - 1] += 1

            if check[num - 1] > 1:
                ans.add(num)

        return ans
        