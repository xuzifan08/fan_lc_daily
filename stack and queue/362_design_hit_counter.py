class HitCounter:

    def __init__(self):
        self.records = dict()
        self.timestamp = collections.deque()

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.timestamp:
            self.timestamp.append(timestamp)
            self.records[timestamp] = 1
        else:
            self.records[timestamp] += 1
        print(self.records)

    def getHits(self, timestamp: int) -> int:
        hits = 0
        for t in self.timestamp:
            if timestamp - 300 < t:
                hits += self.records[t]
        return hits
        