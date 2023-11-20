class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves_left_and_right = ['L', 'R']
        moves_up_and_down = ['U', 'D']

        sum_horinzotal = 0
        sum_vertical = 0

        for move in moves:
            if move in moves_left_and_right:
                sum_horinzotal += 1 if move == 'L' else -1
                continue

            if move in moves_up_and_down:
                sum_vertical += 1 if move == 'U' else -1

        if sum_vertical == 0 and sum_horinzotal == 0:
            return True
        return False
