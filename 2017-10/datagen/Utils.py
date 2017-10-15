import random

class Utils:
    seed = 0

    def setSeed(self,s):
        seed = s
        random.seed(seed)

    def getInt(self):
        print(random.random())
