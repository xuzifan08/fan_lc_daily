class RandomizedSet:

    def __init__(self):
        self.set = []
        self.dict = {}
        # self.set = [val1, val2, val3]
        # self.dict = {val1: index1, val2: index2, val3:index3}
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.set.append(val)
        self.dict[val] = len(self.set) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        index = self.dict[val]
        self.dict[self.set[-1]] = index
        self.set[-1], self.set[index] = self.set[index], self.set[-1]
        self.set.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.set)
        