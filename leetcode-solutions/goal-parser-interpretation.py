class Solution:
    def interpret(self, command: str) -> str:
        flag = True
        res = ''
        for ch in command:
            if ch == 'G':
               res += ch
            elif ch == ')':
                if flag :
                    res += 'o'
                else:
                    res += 'al'
                    flag = True
            elif ch == 'a':
                flag = False


        return res
            


