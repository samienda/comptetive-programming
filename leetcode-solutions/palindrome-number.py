class Solution:
    def isPalindrome(self, x: int) -> bool:
        holdit = x
        newnum = 0
        def count(x):
            if x == 0:
                return 1
            ct = 0
            while x > 0:
                x //= 10
                ct += 1
            return ct


        while x > 0:
            n = count(x)

            newnum += (x % 10) * (10**(n - 1))
            print(newnum, x) 
            x //= 10


        if newnum == holdit:
            return True
        return False