import random
import concurrent.futures

class Dice:
    minValue = 1
    maxValue = 6

    def __init__(self, diceCount):
        self.diceCount = diceCount

    def roll(self):
        totalSum = 0
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(random.randint, self.minValue, self.maxValue) for _ in range(self.diceCount)]
            for f in futures:
                totalSum += f.result()
        return totalSum