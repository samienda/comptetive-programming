class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def calc(maximum):

            sub = 1
            curr = 0
            for num in nums:
                if num > maximum:
                    sub = k + 1
                    break

                if curr + num > maximum:
                    curr = num
                    sub += 1
                else:
                    curr += num

            
            return sub <= k

        
        low = 0
        high = sum(nums)
        
        while low < high:
            mid = (low + high) // 2

            if calc(mid):
                high = mid
            else:
                low = mid + 1

        # print(low)
        return low

        