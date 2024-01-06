class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        ptr = 0

        while ptr < n - 1 and nums[ptr] != '_':
            left = ptr
            right = ptr + 1




            while nums[left] == nums[right]:
               
                nums.pop(right)
                nums.append("_")
                count += 1
               
            ptr += 1


        return n - count

        
        