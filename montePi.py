def montePi(numDarts):

    import random
    import math

    dartsInCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        d = math.sqrt(x**2 + y**2)

        if d<=1:
            dartsInCircle = dartsInCircle + 1

    pi = (dartsInCircle/numDarts) * 4

    return pi