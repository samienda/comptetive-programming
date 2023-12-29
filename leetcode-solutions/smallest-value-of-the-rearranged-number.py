class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = False
        if num < 0 :
            num = str(num * (-1))
            neg = True
        else:
            num = str(num)

        n = len(num)
        num = list(num)

        for i in range(n):
            for j in range(n- 1):
                if not neg and num[j] > num[j + 1]:
                    num[j], num[j + 1] = num[j + 1], num[j]
                    
                if neg and num[j] < num[j + 1]:
                    num[j], num[j + 1] = num[j + 1], num[j]


        if num[0] == '0':
            for i in range(n):
                if num[i] != '0':
                    num[0], num[i] = num[i], num[0]
                    return int("".join(num)) 
                    
        return int("".join(num)) if not neg else int("".join(num)) * (-1)



            
