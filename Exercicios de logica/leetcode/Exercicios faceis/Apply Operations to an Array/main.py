class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i, n in enumerate(nums):
            if i != len(nums) - 1:
                if n == nums[i + 1]:
                    nums.pop(i)
                    nums.pop(i)
                    nums.insert(i, n * 2)
                    nums.append(0)

        for _ in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

        return nums
