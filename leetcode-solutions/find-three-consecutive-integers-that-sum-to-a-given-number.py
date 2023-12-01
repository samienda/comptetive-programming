class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3

        currsum = (3 * x) + 3

        while currsum > num:
            print(currsum, num)
            currsum -= (x + 2)
            x -= 1
            currsum += x

        return [x, x + 1, x + 2] if currsum == num else []