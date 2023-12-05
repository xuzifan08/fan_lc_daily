
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()

    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def dfs(self, nested):
        for n in nested:
            if n.isInteger():
                self.stack.append(n.getInteger())
            else:
                self.dfs(n.getList())



class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.ptr = 0
        self.dfs(nestedList)
        
    def next(self) -> int:
        self.ptr += 1
        return self.list[self.ptr - 1]

    def hasNext(self) -> bool:
        if self.ptr < len(self.list):
            return True
        else:
            False

    def dfs(self, nested):
        for ele in nested:
            if ele.isInteger():
                self.list.append(ele.getInteger())
            else:
                self.dfs(ele.getList())