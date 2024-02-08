class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix = [0] * 1001

        for passengers, start, end in trips:
            prefix[start] += passengers
            prefix[end] -= passengers


        running = 0
        for i in range(1001):
            running += prefix[i]
            prefix[i] = running

            if prefix[i] > capacity:
                return False

        return True


        

            

        