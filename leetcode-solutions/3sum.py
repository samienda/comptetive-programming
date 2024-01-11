class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums.sort()
        res = []
        dic = Counter()

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    value = (nums[i], nums[left], nums[right])
                    if value not in dic:
                        res.append(value)
                        dic[value] = 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1


        return res

                
        