import collections
class RecentCounter:

    def __init__(self):
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        if not self.queue:
            self.queue.append(t)
            return 1
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)