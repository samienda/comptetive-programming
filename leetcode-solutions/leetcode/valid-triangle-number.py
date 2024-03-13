class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        comb = []
        nums.sort()

        for i in range(n - 1, 1, -1):
            for j in range(i - 1, 0, -1):
                comb.append([i, j])

        # print(comb)
        
        count = 0
        for right, mid in comb:
            b = nums[mid]
            c = nums[right]

            left = bisect.bisect_right(nums, c - b)

            if left < mid:
                count += mid - left

            
        
        return count
        