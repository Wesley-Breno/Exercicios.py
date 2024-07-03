class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.array = []

    def push(self, x: int) -> None:
        if len(self.array) < self.maxSize:
            self.array.append(x)

    def pop(self) -> int:
        if len(self.array) >= 1:
            last_value = self.array[-1]
            self.array.pop()
            return last_value
        return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.array) < k:
            self.array = [array_value + val for array_value in self.array]
        else:
            for c in range(k):
                self.array[c] += val
