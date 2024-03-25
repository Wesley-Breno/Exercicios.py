class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum([1 if '++' in x else -1 for x in operations])
