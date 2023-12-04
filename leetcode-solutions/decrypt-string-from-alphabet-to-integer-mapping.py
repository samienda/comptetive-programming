class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''

        n = len(s)


        i = n - 1

        while i >= 0:
            # print(i)

            if s[i] == "#":
                order = ''
                i -= 1
                for _ in range(2):
                    order = s[i] + order
                    i -= 1
            else:
                order = s[i]
                i -= 1

            # print("order", order)

            res =  chr(int(order) + ord('a') - 1) + res

        return res


        

