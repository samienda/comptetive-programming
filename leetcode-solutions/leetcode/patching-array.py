class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:


        i = 1
        running = 0
        j = 0
        oper = 0

        while i < n + 1:
            # print(i)
            
            while j < len(nums) and nums[j] <= i:
                # print("in", running)
                running += nums[j]
                j += 1


            if running < i:
                running += i
                oper += 1

            i = running + 1

        return oper

            

        