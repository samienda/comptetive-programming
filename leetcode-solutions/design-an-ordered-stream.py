class OrderedStream:

    def __init__(self, n: int):
        self.data = [0] * n
        self.pointer = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:    
        self.data[idKey - 1] = value
        res = []

        if idKey - 1 == self.pointer:
            while self.pointer < len(self.data):
                if self.data[self.pointer] != 0:
                    res.append(self.data[self.pointer])
                    self.pointer += 1
                else:
                    break
        return res




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)