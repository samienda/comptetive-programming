class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        greater_side = []
        less_side = []
        equals = []

        for num in nums:
            if num > pivot:
                greater_side.append(num)
            elif num < pivot:
                less_side.append(num)
            else:
                equals.append(num)

        return less_side + equals + greater_side
        