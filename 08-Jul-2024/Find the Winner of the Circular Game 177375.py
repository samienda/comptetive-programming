# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        

        def nex(i):return (i - 1 + k) % len(lis) 
        def remove(i):
            num = lis[i]
            lis.remove(num)

        lis = deque()
        for i in range(1, n + 1):
            lis.append(i)

        curr = 0
        while len(lis) > 1:
            curr = nex(curr)
            # print(lis, curr)
            remove(curr)
            # print(lis)

        return lis[0]
