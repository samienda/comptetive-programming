# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        maxi = max(abs(a), abs(b))
        mini = min(abs(a), abs(b))

        # print()
        dif = maxi.bit_length() - mini.bit_length()
        # print()

        A = list(map(int, bin(maxi)[2:]))
        B = list(map(int, "0" * dif + bin(mini)[2:]))

        def fulladder(a, b):
            # print(a)
            # print(b)
            cin = 0

            answer = []
            while a and b:
                ai = a.pop()
                bi = b.pop()

                s = ai ^ bi ^ cin
                cout = (ai & bi) or (cin & (ai ^ bi))
                cin = cout
                answer.append(str(s))

            if cin:answer.append(str(cin))
            return answer[::-1]

        def fullsubtractor(a, b):
            # print(a)
            # print(b)
            cin = 0

            answer = []
            while a and b:
                ai = a.pop()
                bi = b.pop()

                s = ai ^ bi ^ cin
                cout = (~ai & bi) or (cin & ~(ai ^ bi))
                cin = cout
                answer.append(str(s))

            if cin:answer.append(str(cin))
            return answer[::-1]


        if a >= 0 and b >= 0:
            ans =['0b'] + fulladder(A,B)
        elif a < 0 and b < 0:
            ans =['-0b'] + fulladder(A,B)
        elif maxi == abs(min(a, b)):
            ans =['-0b'] + fullsubtractor(A,B)
        else:
            ans =['0b'] + fullsubtractor(A,B)

        return int("".join(ans), 2)