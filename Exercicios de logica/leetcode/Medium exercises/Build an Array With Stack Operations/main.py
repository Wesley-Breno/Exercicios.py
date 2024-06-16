class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        steps = []
        steps_in_num = []
        for c in range(1, n + 1):
            if c in target:
                steps.append('Push')
                steps_in_num.append(c)
                continue
            if steps_in_num == target:
                return steps
            if c <= n:
                steps.append('Push')
                steps.append('Pop')
        return steps
