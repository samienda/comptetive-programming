class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        days = defaultdict(int)

        for i in range(n):

            while stack and stack[-1][1] < temperatures[i]:
                temp = stack.pop()
                days[temp] = i

            stack.append((i, temperatures[i]))
        # print(days)
        for i in range(n):
            temp = temperatures[i]
            if (i, temp) in days:
                temperatures[i] = days[(i,temp)] - i
            else:
                temperatures[i] = 0     

        return temperatures       

        