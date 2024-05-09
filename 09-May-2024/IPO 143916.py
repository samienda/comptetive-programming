# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        combined = [[capital[i], profits[i]] for i in range(n)]
        combined.sort()

        # print(combined)
        heap = []


        ptr = 0
        for i in range(k):

            while ptr < n and combined[ptr][0] <= w:
                c, p = combined[ptr]
                heapq.heappush(heap, -(p))

                ptr += 1

            if heap:
                w += -heapq.heappop(heap)
            else:
                break
        
        return w