class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            self.stack.append([val, min(val, self.stack[-1][1])])

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]
        
    def getMin(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1][1]
        
