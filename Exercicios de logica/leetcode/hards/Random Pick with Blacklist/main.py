import random


class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        self.range_size = n - len(blacklist)
        self.mapping = {}
        blacklist_set = set(blacklist)

        last_valid = n - 1

        for b in blacklist:
            if b < self.range_size:
                while last_valid in blacklist_set:
                    last_valid -= 1
                self.mapping[b] = last_valid
                last_valid -= 1

    def pick(self) -> int:
        rand = random.randint(0, self.range_size - 1)
        return self.mapping.get(rand, rand)
