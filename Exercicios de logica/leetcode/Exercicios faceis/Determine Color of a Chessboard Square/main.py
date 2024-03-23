class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row, column = coordinates[0], coordinates[1]
        if int(column) % 2 != 0 and row in ['b', 'd', 'f', 'h'] or int(column) % 2 == 0 and row not in ['b', 'd', 'f', 'h']:
            return True
        return False
    