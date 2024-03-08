class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        count = Counter(nums)

        ans = 0
        last = 0
        for key, value in sorted(count.items(), key=lambda item:item[1], reverse=True ):
            if not last or value == last:
                ans += value
                last = value
            else:
                break

        return ans      