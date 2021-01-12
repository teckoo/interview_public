class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = collections.deque()

    def push(self, x: int) -> None:
        if len(self.que) == 0:
            self.que.append((x, x))
        else:
            self.que.append((x, min(x, self.que[-1][1])))

    def pop(self) -> None:
        if len(self.que):
            self.que.pop()

    def top(self) -> int:
        if self.que:
            return self.que[-1][0]        

    def getMin(self) -> int:
        if self.que:
            return self.que[-1][1]
