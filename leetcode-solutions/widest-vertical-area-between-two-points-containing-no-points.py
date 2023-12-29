class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)

        points.sort()

        widest = 0
        for i in range(n - 1):
            widest = max(widest,  points[i + 1][0] - points[i][0])





        return widest