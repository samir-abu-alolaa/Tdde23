import math
def Neg_Gaus_Blur(x, y):
    """ Returns a negative gaussian blur value for coordinates x and y """
    s = 4.5
    return (-1 / (2 * math.pi * s ** 2)) * math.e ** (-(x ** 2 + y ** 2) / (2 * s ** 2))


def unsharp_mask(n):
    """
    Creates negative gaussian blur mask of size n
    """
    return [[1.5 if x == n//2 and y == n//2 else Neg_Gaus_Blur(x - n//2, y - n//2) for x in range(n)] for y in range(n)]
