class Solution:
    def search(self, nums: list[int], target: int) -> int:
        baixo = 0
        alto = len(nums) - 1

        while baixo <= alto:
            meio = int((alto+baixo) / 2)
            chute = nums[meio]
            if chute == target:
                return meio
            elif chute > target:
                alto = meio - 1
            else:
                baixo = meio + 1

        return -1