import random
from collections import Counter


class GameLogic:

    @staticmethod
    def roll_dice(n):
        """
            Roll n number of times
            :param n: number of dice to be rolled
            :return: tuple of 6
        """
        return tuple(random.randint(1, 6) for _ in range(n))


    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculates the score of each dice roll
        :param dice_roll: a tuple that represents the number that's been rolled and the frequency
        :return: integer representing the total score
        """

        if not len(dice_roll):
            return 0
        roll_score = 0
        dice_counter = Counter(dice_roll)
        distinct_dice = len(dice_counter)
        most_common_roll = dice_counter.most_common(1)[0][1]
        if distinct_dice == 6:
            return 1500
        if distinct_dice == 3 and most_common_roll == 2:
            return 1500
        base_scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
        for number_on_dice, frequency in dice_counter.items():
            if frequency >= 3:
                roll_score += base_scores[number_on_dice] * (frequency - 2)
            elif number_on_dice == 1:
                roll_score += 100 * frequency
            elif number_on_dice == 5:
                roll_score += 50 * frequency
        return roll_score
