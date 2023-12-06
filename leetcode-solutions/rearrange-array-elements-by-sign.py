class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)


        res = [0] * n
        neg = 0
        pos = 0
        for num in nums:
            if num < 0:
                res[2 * neg + 1] = num
                neg += 1
            else:
                res[2 * pos] = num
                pos += 1
        return res


        

        
        