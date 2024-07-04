from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles_splited = [letter for letter in tiles]

        all_responses = set()
        for c in range(1, len(tiles_splited) + 1):
            for i in range(1, c + 1):
                all_responses.add(permutations(tiles_splited, r=i))

        wtf = set()
        for a in all_responses:
            for b in a:
                wtf.add(''.join(b))

        return len(wtf)
