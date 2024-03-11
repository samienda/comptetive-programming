class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        stack = []
        mini = 0
        count = 0
        for right in range(n):
            # print(stack, mini)

            
            while stack and height[stack[-1]] >= mini <  height[right]:
                # print(right)
                left = stack[-1]
                if height[left] < height[right]:
                    stack.pop()
                    

                if left + 1 != right:
                    count += ((min(height[left], height[right]) - mini) * (right - left - 1))

                mini = max(mini, height[left])   

            stack.append(right) 
            mini = height[right]

        return count