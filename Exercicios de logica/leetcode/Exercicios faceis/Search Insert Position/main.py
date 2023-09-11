from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        highest_value = max(nums)
        lower_value = min(nums)

        if highest_value < target:
            nums.append(target)
            return nums.index(target)

        if lower_value > target:
            nums.insert(0, target)
            return nums.index(target)

        for index, num in enumerate(nums):
            if num + 1 == target:
                return index + 1
            if num - 1 == target:
                return index
