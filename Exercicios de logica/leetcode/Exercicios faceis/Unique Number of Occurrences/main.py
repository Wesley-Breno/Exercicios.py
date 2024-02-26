from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        existing_values = []
        result = list(Counter(arr).values())
        for number in result:
            if number not in existing_values:
                existing_values.append(number)
                continue
            else:
                return False
        return True
