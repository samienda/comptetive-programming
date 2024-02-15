class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        exchange = defaultdict(int)

        five = 5
        ten = 10
        twenty = 20

        for bill in bills:
            if bill == twenty:
                if exchange[ten] > 0 and exchange[five] > 0:
                    exchange[ten] -= 1
                    exchange[five] -= 1
                elif exchange[five] > 2:
                    exchange[five] -= 3
                else:
                    return False
            elif bill == ten:
                if exchange[five] > 0:
                    exchange[five] -= 1
                else:
                    return False

            exchange[bill] += 1
            # print(exchange)
        return True


        