class MyQueue:

    def __init__(self):
        # stack_1 = [1,2,3]
        # stack_2 = [3,2,]
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        length = len(self.stack_1)
        while length > 1:
            self.stack_2.append(self.stack_1.pop())
            length -= 1
        res = self.stack_1.pop()
        
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())
        
        return res

    def peek(self) -> int:
        return self.stack_1[0]

    def empty(self) -> bool:
        return not self.stack_1
        