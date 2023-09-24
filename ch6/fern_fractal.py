import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def transformation_function(point):
    """
    Applies a transformation rule to the given point.

    Args:
        point (tuple): A tuple representing a point (x, y) in the plane.

    Returns:
        tuple: A new point (x', y') after applying the transformation rule.
    """

    def rule4():
        """Transformation 4 (0.85 probability):"""
        return 0.85 * point[0] + 0.04 * point[1], 0.85 * point[1] + 1.6 - 0.04 * point[0]

    def rule3():
        """Transformation 3 (0.07 probability):"""
        return 0.2 * point[0] - 0.26 * point[1], 0.23 * point[0] + 0.22 * point[1] + 1.6

    def rule2():
        """Transformation 2 (0.07 probability)"""
        return -0.15 * point[0] + 0.28 * point[1], 0.26 * point[0] + 0.24 * point[1] + 0.44

    def rule1():
        """Transformation 1 (0.01 probability):"""
        return 0, 0.16 * point[1]

    rules = [rule1, rule2, rule3, rule4]
    cumulative_prob_sum = [0.01, 0.08, 0.15, 1]
    rand = random.random()

    index_of_applied_trans_rule = 0

    for index, prob in enumerate(cumulative_prob_sum):
        if rand < prob:
            index_of_applied_trans_rule = index
            break

    return rules[index_of_applied_trans_rule]()


def get_xy_points(n):
    """
    Generate a list of x and y points using the transformation function.

    Args:
        n (int): The number of points to generate.

    Returns:
        tuple: A tuple containing two lists, x and y, representing the generated points.
    """
    x = [0]
    y = [0]

    for i in range(n):
        next_point = transformation_function((x[-1], y[-1]))
        x.append(next_point[0])
        y.append(next_point[1])

    return x, y


def draw_fern(n):
    """
    Draw a fern fractal by generating and plotting points.

    Args:
        n (int): The number of points to generate and plot.

    Raises:
        ValueError: If the number of points is less than 1000.

    Returns:
        None
    """
    try:
        if n < 1000:
            raise ValueError(f"Number of points ({n}) is too small; try to increase it, so that it >= 1000.")
    except ValueError as e:
        print(e)
    else:
        points = get_xy_points(n)
        x = points[0]
        y = points[1]
        ax = plt.gca()

        def plot(i):
            ax.plot([x[i]], [y[i]], marker='o', linestyle='', color="blue")

        anim = animation.FuncAnimation(
            plt.gcf(),
            frames=n,
            func=plot,
            interval=0
        )

        plt.show()


draw_fern(5000)
