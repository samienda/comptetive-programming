class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        after = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                after[stack.pop()] = i

            stack.append(i)

        # print(after)

        before = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                before[i] = stack[-1]
            stack.append(i)

        # print(before)
        ans = [((i - before[i])*(after[i] - i) * arr[i]) for i in range(n)]
        # print(ans)


        return sum(ans) %  (10 ** 9 + 7)

            

        