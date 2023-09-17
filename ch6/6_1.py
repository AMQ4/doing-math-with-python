import matplotlib.pyplot as plt


def draw_rectangle(width, height, axes=None):
    """
    Draw a rectangle on the provided axes.

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
        axes (matplotlib.axes.Axes, optional): The axes on which to draw the rectangle. If None, uses the current axes.

    Returns:
        None
    """
    vertices = [(0, 0), (width, 0), (width, height), (0, height)]
    rectangle = plt.Polygon(vertices)
    if axes is None:
        axes = plt.gca()

    axes.set_xlim(0, width)
    axes.set_ylim(0, height)
    axes.add_patch(rectangle)


def draw_circle(w, h, r, axes):
    """
    Draw a circle with the given parameters on the provided axes.

    Args:
        w (float): The x-coordinate of the circle's center.
        h (float): The y-coordinate of the circle's center.
        r (float): The radius of the circle.
        axes (matplotlib.axes.Axes): The axes on which to draw the circle.

    Returns:
        None
    """
    circle = plt.Circle((w, h), r, color="orange")
    axes.add_patch(circle)


def fill_circles(width, height, r, axes):
    """
    Fill the given width and height with circles of the specified radius.

    Args:
        width (float): The width of the area.
        height (float): The height of the area.
        r (float): The radius of the circles.
        axes (matplotlib.axes.Axes): The axes on which to draw the circles.

    Returns:
        None
    """
    num_horizontal_circles = int(width // (r * 2))
    num_vertical_circles = int(height // (r * 2))

    area = num_horizontal_circles * num_vertical_circles

    for i in range(1, num_vertical_circles * 2, 2):
        for j in range(1, num_horizontal_circles * 2, 2):
            draw_circle(r * j, r * i, r, plt.gca())

    print(f"number of circles drawn = {area}")


if __name__ == "__main__":
    draw_rectangle(5, 5, plt.gca())
    fill_circles(5, 5, 0.5, plt.gca())
    plt.gca().set_aspect("equal")
    plt.show()
