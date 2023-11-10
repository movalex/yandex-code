from time import time
from copy import deepcopy


class Stack:
    def __init__(self):
        self.max_heap = MaxHeap()

    def push(self, item):
        t = time()
        self.max_heap.push(item, t)

    def pop(self):
        item = self.max_heap.pop()
        return item

    @property
    def get_data(self):
        temp = deepcopy(self.max_heap)
        try:
            while temp:
                curr = temp.pop()
                print(curr)
        except IndexError:
            pass


import heapq


class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, item, priority):
        heapq.heappush(
            self._heap, (-priority, item)
        )  # store negative timestamp to pop the latest element

    def pop(self):
        item = heapq.heappop(self._heap)
        return item


from time import time


c = Stack()
c.push(56345)
c.push(12)
c.push(12314)
c.push(34543)
c.push(32)
c.get_data
c.pop()
