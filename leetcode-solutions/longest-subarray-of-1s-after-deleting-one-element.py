class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        last = ""
        size = 0
        dic = Counter()


        for right in range(n):
            if nums[right] == 0:
                if last != "":
                    left = last + 1
                last  = right

            
            size = max(size, right - left)

        return size
        