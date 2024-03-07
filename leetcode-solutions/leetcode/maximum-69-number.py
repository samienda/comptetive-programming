class Solution:
    def maximum69Number (self, num: int) -> int:

        nums = list(map(int, str(num)))
        n = len(nums)
        for i in range(n):
            if nums[i] == 6:
                nums[i] = 9
                break

        
        ans = 0
        for num in nums:
            ans = ans * 10 + num

        return ans 
        