class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        list_index = set()
        for index, num in enumerate(nums):
            if len(list_index) > 0:
                break

            for i in range(index):
                if num + nums[i] == target:
                    list_index.add(index)
                    list_index.add(i)
                    break

        return sorted(list_index)


a = Solution()
response = a.twoSum([2222222, 2222222], 4444444)
print(response)
