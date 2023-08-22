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


def total_flight_time(u, theta):
    """
    Calculate the total time of flight for a projectile.

    :param u: Initial velocity in m/s.
    :param theta: Launch angle in degrees.
    :return: Total time of flight in seconds.
    """
    return 2 * u * sin(radians(theta)) / G


def maximum_traveled_horizontal_distance(u, theta):
    """
    Calculate the maximum horizontal distance traveled by a projectile.

    :param u: Initial velocity in m/s.
    :param theta: Launch angle in degrees.
    :return: Maximum horizontal distance in meters.
    """
    return total_flight_time(u, theta) * cos(radians(theta)) * u


def maximum_traveled_vertical_distance(u, theta):
    """
    Calculate the maximum vertical distance traveled by a projectile.

    :param u: Initial velocity in m/s.
    :param theta: Launch angle in degrees.
    :return: Maximum vertical distance in meters.
    """
    return total_flight_time(u, theta)/2 * ( u * sin(radians(theta)) - 0.5 * G * total_flight_time(u, theta)/2)


# Set labels and title for the plot
xlabel("x-coordinate")
ylabel("y-coordinate")
title("Projectile motion")
