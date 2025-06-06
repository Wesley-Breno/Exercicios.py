import random

class Solution:
    def __init__(self, nums: list[int]):
        self.original = nums[:]

    def reset(self) -> list[int]:
        return self.original[:]

    def shuffle(self) -> list[int]:
        arr = self.original[:]
        for i in range(len(arr)):
            j = random.randint(i, len(arr) - 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
