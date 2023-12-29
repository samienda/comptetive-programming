class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)

        nums = sorted(arr)
        
        res = []
        for j in range(n - 1, -1, -1):
            idx = arr.index(nums[j])
            if idx == j:
                continue

            arr = arr[idx::-1] + arr[idx + 1:]
            arr = arr[j::-1] + arr[j + 1:]
            


            res.append(idx + 1)
            res.append(j + 1)

            if arr == nums:
                return res



        
        return res
