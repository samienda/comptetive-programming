class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 2)


        for first, last, seat in bookings:
            prefix[first] += seat
            prefix[last + 1] -= seat


        running = 0
        for i in range(1, n + 1):
            running += prefix[i]
            prefix[i] = running

        return prefix[1:n + 1]
        