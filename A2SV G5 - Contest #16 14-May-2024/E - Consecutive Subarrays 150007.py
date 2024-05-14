# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

n, k = list(map(int, input().split()))
array = list(map(int, input().split()))

suffix = array[:]
for i in range(n - 2, -1, -1):
    suffix[i] += suffix[i + 1]


ans = suffix[0] + sum(sorted(suffix[1:], reverse=True)[:k - 1])

print(ans)
