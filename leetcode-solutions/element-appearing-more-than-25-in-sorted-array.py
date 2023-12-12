class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = {}
        n = len(arr)
        quarter = n // 4

        for num in arr:
            dic[num] = 1 + dic.get(num, 0)

        return sorted(dic.items(),key=lambda item:item[1], reverse=True)[0][0]         