class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)


        left = 0
        _max = 0
        _sum = 0
        unique = Counter()


        for right in range(n):
            _sum += nums[right]

            while nums[right] in unique:
                _sum -= nums[left]
                unique.pop(nums[left])
                left += 1

            unique[nums[right]] += 1
            _max = max(_max, _sum)

        return _max