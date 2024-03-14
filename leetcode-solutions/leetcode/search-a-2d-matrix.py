class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        def findrow(low, high):
            mid = (low + high) // 2
            if high <= low:
                return high

            # print(mid)

            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                return mid

            return findrow(low, high)

        row = findrow(0, n - 1)
        
        # print(row)
        # return False
        
        def findelem(left, right):
            if left > right:
                return False

            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return True

            return findelem(left, right)

        nums = matrix[row]
        return findelem(0, m - 1)
            