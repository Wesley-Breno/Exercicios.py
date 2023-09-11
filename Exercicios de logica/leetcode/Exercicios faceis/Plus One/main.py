class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer_str = ''
        for num in digits:
            integer_str += str(num)

        integer_plus_one = int(integer_str) + 1

        integer_with_sum = [int(num) for num in str(integer_plus_one)]

        return integer_with_sum
