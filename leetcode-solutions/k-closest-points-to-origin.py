class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def compare(item):
            return ((item[0]**2) + (item[1]**2))**(1/2)


        points.sort(key=compare)



        point = [points[i] for i in range(k)]

        return point
        