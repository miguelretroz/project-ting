from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not len(self):
            return None

        return self._data.popleft()

    def search(self, index):
        if 0 <= index <= (len(self) - 1):
            return self._data[index]
        else:
            raise IndexError
