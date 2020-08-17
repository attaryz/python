import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        # you can return a tuple without typing the ()
        return first, second


dice = Dice()
print(dice.roll())

