class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)


        zeros = []
        left = 0
        size = 0


        for right in range(n):
            if nums[right] == 0:
                zeros.append(right)
                if len(zeros) > k:

                    last = zeros.pop(0)
                    left = last + 1

            size = max(size, right - left + 1)
        
        return size
                
