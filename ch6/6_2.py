"""
#2: Drawing the Sierpiński Triangle

The Sierpiński triangle, named after the Polish mathematician Wacław
Sierpiński, is a fractal that is an equilateral triangle composed of smaller
equilateral triangles embedded inside it.
Your challenge here is to write a program that draws the
Sierpiński triangle composed of a certain number of points specified as
input.
"""

import random
from matplotlib import pyplot as plt


def transformation_function(point):
    """
    Apply a random transformation rule to a given point.

    Args:
        point (tuple): A tuple representing the (x, y) coordinates of the point.

    Returns:
        tuple: A tuple representing the new (x, y) coordinates after applying a transformation rule.
    """

    def rule1():
        """Apply transformation rule 1."""
        return 0.5 * point[0], 0.5 * point[1]

    def rule2():
        """Apply transformation rule 2."""
        return 0.5 * point[0] + 0.5, 0.5 * point[1] + 0.5

    def rule3():
        """Apply transformation rule 3."""
        return 0.5 * point[0] + 1, 0.5 * point[1]

    rules = [rule1, rule2, rule3]

    return random.choice(rules)()


def get_xy_points(n):
    """
    Generate a sequence of (x, y) points using the transformation function.

    Args:
        n (int): The number of points to generate.

    Returns:
        tuple: A tuple containing two lists, one for x-coordinates and one for y-coordinates of the generated points.
    """

    x = [0]
    y = [0]

    for i in range(n):
        next_point = transformation_function((x[-1], y[-1]))
        x.append(next_point[0])
        y.append(next_point[1])

    return x, y


def draw_fractal(n):
    """
    Generate and display a fractal by plotting a sequence of points.

    Args:
        n (int): The number of points to generate for the fractal.

    Raises:
        ValueError: If n is less than 10000, it raises an error as it is too small for meaningful fractal generation.
    """

    try:
        if n < 10000:
            raise ValueError(f"Number of points ({n}) is too small; try to increase it, so that it >= 10000.")
    except ValueError as e:
        print(e)
        return

    points = get_xy_points(n)
    x = points[0]
    y = points[1]

    plt.plot(x, y, marker='o', linestyle='')
    plt.show()


draw_fractal(10000)
