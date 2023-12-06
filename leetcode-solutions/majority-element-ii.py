class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)


        max_appear = n // 3
        result = []
        appear = {}

        for i in range(n):
            appear[nums[i]] = 1 + appear.get(nums[i], 0)

            if appear[nums[i]] > max_appear and nums[i] not in result:
                result.append(nums[i])


        return result

        