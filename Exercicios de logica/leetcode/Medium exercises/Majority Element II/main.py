class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        numbers = set()
        for n in nums:
            if nums.count(n) > len(nums) / 3:
                numbers.add(n)
        return list(numbers)

