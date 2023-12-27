class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        dic = {}
        res = []
        second = set(arr2)
        last = []

        for num in arr1:
            if num not in second:
                last.append(num)
            else:
                dic[num] = 1 + dic.get(num, 0)

        # print(dic)
        for num in arr2:
            n = dic[num]
            nums = [num] * n
            res += nums
            dic.pop(num)


        last.sort()
        return res + last


        



        print(dic)
        return []