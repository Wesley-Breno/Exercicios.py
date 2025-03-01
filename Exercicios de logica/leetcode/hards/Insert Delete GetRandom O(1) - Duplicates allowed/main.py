from random import choice


class RandomizedCollection:
    def __init__(self):
        self.set = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            self.set.append(val)
            return False
        self.set.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.set)