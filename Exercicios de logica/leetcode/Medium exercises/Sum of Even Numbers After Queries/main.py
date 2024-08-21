class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        soma = sum(num for num in nums if num % 2 == 0)
        response = []
        for value, index in queries:
            if nums[index] % 2 == 0:
                soma -= nums[index]
            nums[index] += value
            if nums[index] % 2 == 0:
                soma += nums[index]
            response.append(soma)
        return response
