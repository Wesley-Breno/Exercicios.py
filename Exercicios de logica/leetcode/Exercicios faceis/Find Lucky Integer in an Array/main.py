from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        try:
            return max([key for key, value in Counter(arr).items() if key == value])
        except:
            return -1
