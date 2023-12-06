class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        step = 0
        for i in range(1, n):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            step +=  max(abs(x2 - x1), abs(y2 - y1))
            
                  
        return step