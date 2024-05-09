# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], eff: List[int], k: int) -> int:
        n = len(speed)

        combined = [[eff[i], speed[i]] for i in range(n)]
        combined.sort(reverse=True)

        totalspeed = 0
        performance = 0

        # print(combined)

        heap = []
        for e, s in combined:

            heapq.heappush(heap, s)
            totalspeed += s

            if len(heap) > k:
                totalspeed -= heapq.heappop(heap)

            performance = max(performance, totalspeed * e)

        return performance % (10**9 + 7)
