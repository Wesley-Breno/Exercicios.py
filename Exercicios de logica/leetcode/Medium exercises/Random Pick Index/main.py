import random


class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.indexes = dict()
        for i, num in enumerate(nums):
            try:
                self.indexes[num].append(i)
            except KeyError:
                self.indexes[num] = [i]

    def pick(self, target: int) -> int:
            return random.choice(self.indexes[target])