class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)


        right = 0
        left = 0
        odd = []
        count = 0



        while right < n:
            if nums[right] % 2 != 0:
                k -= 1
                odd.append(right)
            


            
            while k < 0:
                if nums[left] % 2 != 0:
                    k += 1
                    odd.pop(0)

                left += 1


            if k == 0:
                value = odd[0] - left + 1
                count += value

            right += 1

        return count
