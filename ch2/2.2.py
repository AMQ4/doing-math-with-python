import matplotlib.pyplot as plt


def graph(a, b, c):
    """
    Plot a quadratic equation y = ax^2 + bx + c and visualize its graph.

    :param float a: Coefficient of the x^2 term.
    :param float b: Coefficient of the x term.
    :param float c: Constant term.
    """

    def f_x(x):
        return a * (x ** 2) + b * x + c

    # Calculate the x-coordinate of the vertex
    h_coor = -b / (2 * a)

    # Generate x and y values for plotting
    y, x = [], []
    for i in range(-10, 11):
        x_value = h_coor + i
        x.append(x_value)
        y.append(f_x(x_value))

    # Set up the plot
    plt.title("Quadratic Equation Graph")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis(ymax=max(y), xmin=min(x), xmax=max(x))

    # Plot the graph and show
    plt.plot(x, y, marker='o')
    plt.show()


# Get coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter constant c: "))

# Generate and display the graph
graph(a, b, c)
