import numpy as np

def correlation(x, y):
    try:
        if(len(x) != len(y)):
            raise ValueError("Input lists must have the same length for correlation calculation.\n")
    except ValueError as e:
        print(e)
        return 0
    else:
        xy = [_x * _y for _x, _y in zip(x, y)]
        x2 = [_x * _x for _x in x]
        y2 = [_y * _y for _y in y]
        n = len(x)
        sumx = sum(x)
        sumy = sum(y)
        sumxy = sum(xy)
        sumx2 = sum(x2)
        sumy2 = sum(y2)

        return (n * sumxy - sumx * sumy)/((n * sumx2 - sumx**2) * (n * sumy2 - sumy**2)) **0.5
