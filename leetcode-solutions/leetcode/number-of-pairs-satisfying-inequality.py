class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        def merge(lefthalf, righthalf):

            left = 0
            right = 0
            count = 0
            curr = 0

            newlis = []
            queue = deque(lefthalf)
            while left < len(lefthalf) and right < len(righthalf):
                # print(lefthalf, righthalf, curr, count, newlis, queue)

                if lefthalf[left] > righthalf[right]:
                    newlis.append(righthalf[right])

                    while queue and queue[0] <= righthalf[right] + diff:
                        curr += 1
                        queue.popleft()

                    count += curr
                    right += 1
                else:
                    newlis.append(lefthalf[left])
                    left += 1

            while left < len(lefthalf):
                # print(lefthalf, righthalf, curr, count, newlis, queue)
                newlis.append(lefthalf[left])
                left += 1
                    
           
            while right < len(righthalf):
                # print(lefthalf, righthalf, curr, count, newlis, queue)
                newlis.append(righthalf[right])
                
                while queue and queue[0] <= righthalf[right] + diff:
                    queue.popleft()
                    curr += 1

                count += curr
                right += 1

            # print(lefthalf, righthalf, curr, count, newlis, queue)
            return newlis, count
                
        
        def divide(left, right, nums):
            if left == right:
                return [nums[left]], 0

            mid = (left + right) // 2

            lefthalf, leftcount = divide(left, mid, nums)
            righthalf, rightcount = divide(mid + 1, right, nums)

            combined, combinedcount = merge(lefthalf, righthalf)
            return combined, leftcount + combinedcount + rightcount


        n = len(nums1)
        nums = [0] * n
        for i in range(n): # O(n)

            nums[i] = nums1[i] - nums2[i]


        # print(nums)
        nums, count = divide(0, n - 1, nums)
        # print(nums, count)
        return count