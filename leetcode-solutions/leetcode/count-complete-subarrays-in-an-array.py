class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        need = set(nums)
        have = set()
        freq = Counter()


        left = 0
        count = 0
        for right in range(n):
            freq[nums[right]] += 1
            have.add(nums[right])

            while have == need:
                count += n - right

                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    have.remove(nums[left])
                
                left += 1

        return count


        