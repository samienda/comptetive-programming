class Solution:
    def isHappy(self, n: int) -> bool:



        while 1 <= n <= 2**31:
            s = str(n)
    
            if len(s) == 1:
                return s == '1' or s == '7'
            
            n = 0
            for i in s:
                n += (int(i))**2
 

    

            

        