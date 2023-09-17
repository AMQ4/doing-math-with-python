# Import necessary modules
from matplotlib import animation
from ch2 import ProjectileMotion
from math import radians
import matplotlib.pyplot as plt

# Constants for circle radius and velocity factor
RADIUS_FACTOR = 1.105705440070765
VELOCITY_FACTOR = 12.814310051107326e-05


# Function to update the position of the circle in each frame
def update(i, circle, centers):
    """
    Update the position of the circle in each animation frame.

    :param i: Frame index.
    :param circle: The circle patch representing the projectile.
    :param centers: A tuple containing lists of x and y coordinates.
    :return: The updated circle.
    """
    circle.center = centers[0][0], centers[1][0]
    if len(centers[0]) != 0:
        centers[0].pop(0)
        centers[1].pop(0)
    return circle


# Main program starts here
if __name__ == "__main__":
    # Get user input for initial velocity and launch angle
    u = float(input("Enter the initial velocity (m/s):\n> "))
    theta = float(input("Enter the angle of projection in [0, 90](degrees):\n> "))

    # Handle negative velocity and zero velocity cases
    u = u * -1 if u < 0 else u
    u += 1 if u == 0 else 0

    try:
        # Check if the entered angle is within the valid range
        if theta not in range(0, 91):
            raise ValueError("Invalid angle, the angle is out of range of [0, 90].")

        theta += 1 if theta == 0 else 0
    except ValueError as e:
        print(e)
        exit(1)

    # Calculate the time step for the animation
    ProjectileMotion.time_step = VELOCITY_FACTOR * ProjectileMotion.total_flight_time(u,
                                                                                      theta) / ProjectileMotion.time_step

    # Get the x and y coordinates of the projectile's trajectory
    xy_distances = list(ProjectileMotion.get_Dx_Dy_(u, radians(theta)))

    # Calculate the plot limits (x and y axes)
    xmax = ProjectileMotion.maximum_traveled_horizontal_distance(u, theta) + (-50 if theta in range(90, 271) else 50)
    ymax = ProjectileMotion.maximum_traveled_vertical_distance(u, theta) + 50

    # Create a circle representing the projectile
    circle = plt.Circle((0, 0), RADIUS_FACTOR / 100 * (xmax + ymax))

    # Set up the plot and add the circle
    axes = plt.gca()
    axes.set_xlim(0, xmax)
    axes.set_ylim(0, ymax)
    axes.add_patch(circle)
    axes.set_aspect('equal')

    # Create the animation using FuncAnimation
    anim = animation.FuncAnimation(
        plt.gcf(),
        update,
        fargs=(circle, xy_distances,),
        frames=len(xy_distances[0]) - 1,
        interval=1,
        repeat=False
    )

    # Display the animation
    plt.show()
