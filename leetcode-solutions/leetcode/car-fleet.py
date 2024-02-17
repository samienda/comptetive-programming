class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(speed)
        combine = [[position[i], speed[i]] for i in range(n)]
        combine.sort()
        # print(combine)
        fleet = 0

        def find(target, position, speed):
            time = (target - position ) / speed
            return time


        for position, speed in combine:
        
            while stack and find(target, position, speed) >= find(target, stack[-1][0], stack[-1][1]):
                    back, fast = stack.pop()
                    postion = (fast * position - speed * back) / (fast - speed)
                    # print(stack)
                    
            
            stack.append([position, speed])
                    
                
        # print(stack)

        return len(stack)

