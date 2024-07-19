from itertools import combinations


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self._prepare_data(characters, combinationLength)

    def _prepare_data(self, characters: str, length: int):
        self.characters = []
        for combination in combinations([letter for letter in characters], length):
            self.characters.append(''.join(combination))

    def next(self) -> str:
        next_item = self.characters[0]
        self.characters = self.characters[1:]
        return next_item

    def hasNext(self) -> bool:
        if len(self.characters) > 0:
            return True
        return False
