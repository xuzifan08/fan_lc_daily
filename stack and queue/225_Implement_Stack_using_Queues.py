class MyStack:

    def __init__(self):
        #. queue_1 = [1,2,3]
        #  queue_2 = []
        self.queue_1 = collections.deque()
        self.queue_2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        length = len(self.queue_1)

        while length > 1:
            self.queue_2.append(self.queue_1.popleft())
            length -= 1
        res = self.queue_1.popleft()

        while self.queue_2:
            self.queue_1.append(self.queue_2.popleft())

        return res

    def top(self) -> int:

        return self.queue_1[-1]


    def empty(self) -> bool:
        return not self.queue_1