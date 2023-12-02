class Solution:
    def romanToInt(self, s: str) -> int:
        
        n = len(s)
        num = 0

        for i in range(n):
            ch = s[i]
            if ch == 'I':
                num += 1
            elif ch == 'V':
                if  i != 0 and s[i - 1] == 'I':
                    num += 3
                else:
                    num += 5
            elif ch == 'X':
                if  i != 0 and s[i - 1] == 'I':
                    num += 8
                else:
                    num += 10
            elif ch == 'L':
                if  i != 0 and s[i - 1] == 'X':
                    num += 30
                else:
                    num += 50
            elif ch == 'C':
                if  i != 0 and s[i - 1] == 'X':
                    num += 80
                else:
                    num += 100
            elif ch == 'D':
                if  i != 0 and s[i - 1] == 'C':
                    num += 300
                else:
                    num += 500
            elif ch == 'M':
                if  i != 0 and s[i - 1] == 'C':
                    num += 800
                else:
                    num += 1000


        return num

