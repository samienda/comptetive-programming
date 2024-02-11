from bisect import bisect_left

mod = 10 ** 9 + 7


def countingOrders():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    
    for i in range(n):
        if a[i] <= b[i]:
            print(0)
            return
        
        
    ans = 1
    for i in range(n):
        val = a[i]
        index = bisect_left(b, val)
        index -= i
        ans = (ans* index) % mod
        
    print(ans)
    
    
t = int(input())
for i in range(t):
    countingOrders()