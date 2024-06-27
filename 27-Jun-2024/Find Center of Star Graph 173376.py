# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        n = 1 + len(edges)
        incoming = [0 for i in range(n)]

        for u, v in edges:
            incoming[u - 1] += 1
            incoming[v - 1] += 1

        return incoming.index(n - 1 ) + 1
