"""
#3: Exploring Hénon’s Function

Your challenge here is to write a program to create a graph showing
20,000 iterations of this transformation, starting with the point (1, 1).
Extra credit for writing another program to create an animated figure
showing the points starting to lie along the curves!
"""

import matplotlib.pyplot as plt
from matplotlib import animation


def transformation_function(point):
    """
    Apply the Hénon's Function transformation to a given point.

    Args:
        point (tuple): A tuple containing the (x, y) coordinates of the point.

    Returns:
        tuple: A tuple containing the new (x, y) coordinates after the transformation.
    """
    return point[1] + 1 - 1.4 * point[0] ** 2, 0.3 * point[0]


def get_xy_points(n):
    """
    Generate the (x, y) coordinates of points using Hénon's Function transformation.

    Args:
        n (int): The number of points to generate.

    Returns:
        tuple: A tuple containing two lists, one for x-coordinates and one for y-coordinates.
    """
    x = [1]
    y = [1]

    for i in range(n):
        next_point = transformation_function((x[-1], y[-1]))
        x.append(next_point[0])
        y.append(next_point[1])

    return x, y


def plot_henons_function(n):
    """
    Create a graph showing the iterations of Hénon's Function transformation.

    Args:
        n (int): The number of points to draw in the graph.
    """
    try:
        if n < 1000:
            raise ValueError(f"Number of points ({n}) is too small; try to increase it so that it's >= 1000.")
    except ValueError as e:
        print(e)
        return

    points = get_xy_points(n)
    x = points[0]
    y = points[1]

    ax = plt.gca()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.4, 0.4)

    def plot(i):
        ax.plot([x[i]], [y[i]], marker='o', linestyle='', color="blue")

    animate = animation.FuncAnimation(
        fig=plt.gcf(),
        frames=len(x),
        func=plot,
        interval=100
    )
    plt.show()


plot_henons_function(20_000)
