class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)

        curr = ''
        count = 0


        left = 0
        for right in range(k - 1 , n):
            curr= s[left: right + 1]
    
            if int(curr) != 0 and num % int(curr) == 0:
                count += 1


            left += 1


        return count
