# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)

        graph = defaultdict(list)
        for i, num in enumerate(arr):
            graph[num].append(i)


        dp = [1 for i in range(n)]

        for i, num in enumerate(arr):
            newnum = num + difference

            if newnum in graph:
                for nbs in graph[newnum]:
                    if nbs > i:
                        dp[nbs] = max(dp[nbs], dp[i] + 1)


        return max(dp)