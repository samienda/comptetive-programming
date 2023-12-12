class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
      
        totalsum = sum([i for i in nums if i % 2 == 0])

        ans = []
        for val, index in queries:
            before = nums[index]
            nums[index] += val
            curr = nums[index]

            if before % 2 == 0:
                totalsum -= before
            
            if curr % 2 == 0:
                totalsum += curr

            ans.append(totalsum)

          

        return ans if ans else [0]
        




