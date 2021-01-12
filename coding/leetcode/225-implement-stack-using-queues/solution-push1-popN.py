import collections


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = collections.deque()
        self.que2 = collections.deque()
        self.cur_que = 1

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.cur_que == 1: 
            self.que1.append(x)
        else:
            self.que2.append(x)

    def _pop(self, que1, que2, top=False) -> int:
        last_node = 0
        while len(que1)>0:
                last_node = que1.popleft()
                if len(que1) > 0:
                    que2.append(last_node)
                elif top:
                    que2.append(last_node)

        return last_node

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.cur_que == 1:
            last_node = self._pop(self.que1, self.que2)
            self.cur_que = 2
        else:
            last_node = self._pop(self.que2, self.que1)
            self.cur_que = 1
        # print(f"{self.cur_que}, last_node={last_node}, que1 size = {len(self.que1)}, que2 size={len(self.que2)}")
        return last_node

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.cur_que == 1:
            last_node = self._pop(self.que1, self.que2, top=True)
            self.cur_que = 2
        else:
            last_node = self._pop(self.que2, self.que1, top=True) 
            self.cur_que = 1
        # print(f"{self.cur_que}, que1 size = {len(self.que1)}, que2 size={len(self.que2)}")
        return last_node

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que1) == 0 and len(self.que2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
