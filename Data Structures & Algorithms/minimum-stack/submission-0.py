class MinStack:

    def __init__(self):
        self.stack = [(None,float("inf"))]
        self.next = None

    def push(self, val: int) -> None:
        self.stack.append((val, min(val,self.getMin())))
        

    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
