# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}
        def pick( mask, idx):
            if idx >= len(nums1):return 0

            state = (mask, idx)

            if state not in memo:
                found = 10**9
                for i in range(len(nums1)):
                    # print(mask, 1 << i)
                    if (mask & 1 << i) == 0:
                        # print(idx, i)
                        found = min(
                            found, 
                            pick(
                                mask ^ 1 << i, idx + 1) + \
                                (nums1[idx] ^nums2[i])
                            )
                
                memo[state] = found
            return memo[state]

        return pick(0, 0)
