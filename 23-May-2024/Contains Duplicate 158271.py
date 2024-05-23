# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        last = -1
        for num in nums:
            if num == last:
                return True

            last = num

        return False