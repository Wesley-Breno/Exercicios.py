from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cont_arr = dict(Counter(arr))
        new_dict = dict()
        for key, value in cont_arr.items():
            new_dict[key] = int((value / len(arr)) * 100)

        new_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
        for key, value in new_dict.items():
            if value >= 25:
                return key
