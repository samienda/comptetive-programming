class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        ordered = sorted(nums)

        if nums == ordered:
            return 0
            
        left = 0 
        right = n - 1
        for i in range(n):
            if nums[i] != ordered[i]:
                left = i
                break
                
        for i in range(n - 1, left, -1):
            if nums[i] != ordered[i]:
                right = i
                break
        
        return right - left + 1