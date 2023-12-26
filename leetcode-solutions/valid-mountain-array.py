class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3:
            return False

        increase = True
        for i in range(n - 1):
            if not increase and arr[i] <= arr[i + 1]:
                return False

            if increase and arr[i] >= arr[ i + 1]:
                if i == 0 or arr[i] == arr[i + 1]:
                    return False
                increase = False
                


        return True if not increase else False

        