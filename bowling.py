class Game:

    def __init__(self):
        self._rolls = [0] * 21
        self._current_roll = 0

    def roll(self, pins):
        self._rolls[self._current_roll] = pins
        self._current_roll += 1

    def score(self):
        roll_index = 0
        score = 0
        for frame in range(10):
            if self._is_strike(roll_index):  # strike
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            # elif self._is_spare(roll_index):
            #     score += 10 + self._spare_bonus(roll_index)
            #     roll_index += 2
            else:
                score += self._frame_score(roll_index)
                roll_index += 2
        return score

    def _frame_score(self, roll_index):
        return self._rolls[roll_index] + self._rolls[roll_index + 1]

    def _is_strike(self, roll_index):
        is_strike = self._rolls[roll_index] == 10
        return is_strike

    def _strike_bonus(self, roll_index):
        return self._rolls[roll_index + 1] + self._rolls[roll_index + 2]

    def _is_spare(self, roll_index):
        return self._frame_score(roll_index) == 10

    def _spare_bonus(self, roll_index):
        return self._rolls[roll_index + 2]
