class MinStack:

    def __init__(self):
        self.val = [(None,float("inf"))]
                
    def push(self, val: int) -> None:
        mini = min(self.getMin(),val)
        self.val.append((val,mini))

    def pop(self) -> None:
        self.val.pop()
        

    def top(self) -> int:
        return self.val[-1][0]        

    def getMin(self) -> int:
        return self.val[-1][1]
        
