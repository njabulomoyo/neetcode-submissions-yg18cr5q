class MinStack:
    """
    Solution should run in O(1)  -  we cant iterate thru the list to get the min

    Plan:
        1. initialize a list
        2. have a tuple or list to store the number added and the minimum number of the list at that point
        3. then when poping, remove the whole thing
        4. checking top element, return the number add from the top tuple
        5. getmin will just return the minumum number, which will be the minimum number of the tuple at the top
    """

    def __init__(self):
        self.stack = [(None,float("inf"))]
        

    def push(self, val: int) -> None:
        return self.stack.append((val,min(self.stack[-1][1],val)))
        

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
