class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        all_nums = []
        for a in strs:
            if a.isdigit():
                all_nums.append(int(a))
                continue
            all_nums.append(len(a))
        return max(all_nums)
