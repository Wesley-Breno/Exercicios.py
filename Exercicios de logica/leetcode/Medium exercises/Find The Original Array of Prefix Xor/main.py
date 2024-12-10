class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = []
        for i, v in enumerate(pref):
            if i == 0:
                arr.append(v)
                continue
            arr.insert(i, pref[i] ^ pref[i - 1])
        return arr