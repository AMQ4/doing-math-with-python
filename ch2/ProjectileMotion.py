from matplotlib.pyplot import *
from math import *

# Acceleration due to gravity (in m/s^2)
G = 9.8

def get_Dx_Dy_(U: float, theta: float) -> tuple:
    """
    Calculate the x and y coordinates of a projectile's trajectory.

    :param U: Initial velocity of the projectile (in m/s).
    :param theta: Launch angle in radians.
    :return: Tuple containing lists of x and y coordinates.
    """
    def Dy(t: float) -> float:
        """
        Calculate the vertical displacement at time t.

        :param t: Time (in seconds).
        :return: Vertical displacement at time t.
        """
        return t * (U * sin(theta) - 0.5 * G * t)

    def Dx(t: float) -> float:
        """
        Calculate the horizontal displacement at time t.

        :param t: Time (in seconds).
        :return: Horizontal displacement at time t.
        """
        return t * U * cos(theta)

    t = 0
    t_peak = 2 * U * sin(theta) / G
    y = []
    x = []
    while t < t_peak:
        x.append(Dx(t))
        y.append(Dy(t))
        t += 0.001
    return (x, y)

# Set labels and title for the plot
xlabel("x-coordinate")
ylabel("y-coordinate")
title("Projectile motion")

# List of initial velocities
u_list = [20, 40, 60]
theta = 45  # Launch angle in degrees

# Plot the trajectories for different initial velocities
for u in u_list:
    y_x_value = get_Dx_Dy_(u, radians(45))  # Get x and y values using the method
    plot(y_x_value[0], y_x_value[1])  # Plot the trajectory

# Add a legend to the plot
legend(["at 20 m/s", "at 40 m/s", "at 60 m/s"])

# Display the plot
show()
