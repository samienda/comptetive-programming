class MinStack:

    def __init__(self):
        self.increasing = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.increasing or self.increasing[-1] >= val:
            self.increasing.append(val)
        

    def pop(self) -> None:
        curr = self.stack.pop()
        
        if curr == self.increasing[-1]:
            self.increasing.pop()
        return curr


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.increasing[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()