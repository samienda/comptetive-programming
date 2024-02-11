t = int(input())


def msum():
    prefix = [0]
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    psum = 0
    a.sort()
    ans = 0
    for i in range(n):
        psum += a[i]
        prefix.append(psum)
    # print(prefix)

    for i in range(k + 1):
        lows = prefix[2 * i]
        highs = prefix[n - (k - i)]
        ans = max(ans, highs - lows)

    print(ans)


for i in range(t):
    msum()