class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def calc(divisor):

            ans = 0

            for num in nums:
                ans += math.ceil(num / divisor)

            return ans

        low = 1
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2

            trial = calc(mid)
            if trial > threshold:
                low = mid + 1
            else:
                high = mid

        # print(low, high)
        return low
        