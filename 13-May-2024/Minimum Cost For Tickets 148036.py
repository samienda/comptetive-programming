# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        memo = {}
        def pick(idx):
            # print(idx)
            if idx >= days[-1]:return 0


            idx = bisect.bisect_right(days, idx)
            if idx >= len(days):return 0
            idx = days[idx] - 1

            if idx not in memo:
                memo[idx] = min(
                    pick(idx + 1) + costs[0], 
                    pick(idx + 7) + costs[1], 
                    pick(idx + 30) + costs[2]
                    )
            return memo[idx]

        return pick(0)