class Solution:
    def get_divisors_of_a_number(self, number: int) -> list:
        divisors = []
        for num in range(1, number + 1):
            if number % num == 0:
                divisors.append(num)
        return divisors

    def captures_divisor_filtering_between_two_lists(self, list1: list, list2: list) -> set:
        all_divisors = set()
        lists_mescled = list1 + list2
        for num in lists_mescled:
            if num in list1 and num in list2:
                all_divisors.add(num)
        return all_divisors

    def commonFactors(self, a: int, b: int) -> int:
        divisors_a = self.get_divisors_of_a_number(a)
        divisors_b = self.get_divisors_of_a_number(b)
        return len(self.captures_divisor_filtering_between_two_lists(divisors_a, divisors_b))
