class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

       
        leftelem = []

        for l in range(n):
            if nums[l] % 2 == 0:
                leftelem.append(l)

        if len(leftelem) > 0:
            left = leftelem.pop(0)
        else:
             return 0
        
        count = 0
        k = left
        for right in range(k, n):
            if (nums[right] % 2) == (nums[right - 1] % 2) or  nums[right - 1]  > threshold:               
                left = right

            if  nums[right] > threshold:
                left =  right + 1

            while left < n and nums[left] % 2 != 0:
                left += 1

                

            count = max(count, right - left + 1) 

            


        return count


        