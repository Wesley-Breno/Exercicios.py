class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num_reversed = int(str(num)[::-1])

        if int(str(num_reversed)[::-1]) == num:
            return True
        return False
