class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([1 for stone in stones if stone in jewels])
