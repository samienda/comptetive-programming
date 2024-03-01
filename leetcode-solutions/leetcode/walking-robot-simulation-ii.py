class Robot:

    def __init__(self, width: int, height: int):
        self.direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.currdxn = 0
        self.currpos = [0, 0]
        self.n = width
        self.m = height

    def step(self, num: int) -> None:
        if not num:
            return 
        # print(num)
        row, col = self.currpos
        if num > ((self.m + self.n - 2) * 2) and ( row == 0 or col == 0 or row == self.n - 1 or col == self.m - 1):
            print(self.currpos, self.currdxn)
            num %= ((self.m + self.n - 2) * 2)
            if row == 0 and col == 0:
                self.currdxn = 3
                
        x, y = self.direction[self.currdxn]

        if 0 <= num * x + row < self.n and 0 <= num * y + col < self.m:
            self.currpos = [num * x + row, num * y + col]
        else:
            
            # print(num, self.currpos, self.currdxn)
            if x == 1:
                self.currpos = [self.n - 1, col]
                num -= (self.n - row - 1)
            elif x == -1:
                self.currpos = [0, col]
                num -=  row 
            elif y == 1:
                self.currpos = [row, self.m - 1]
                num -= (self.m - col - 1)
            elif y == -1:
                self.currpos = [row, 0]
                num -=  col
            # if not num:
            #     return
            
            self.currdxn += 1
            self.currdxn %= 4
            return self.step(num)
        

    def getPos(self) -> List[int]:
        return self.currpos
        

    def getDir(self) -> str:
        return ['East', 'North', 'West', 'South'][self.currdxn]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()