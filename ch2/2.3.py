from matplotlib.pyplot import *
from math import *
import ProjectileMotion

def exexperiment_report(u, theta):
    """
    Calculate and display experiment report for a projectile motion experiment.

    :param float u: Initial velocity in m/s.
    :param float theta: Launch angle in degrees.
    """
    print("Time of flight: {0:.2f}".format(ProjectileMotion.total_flight_time(u, theta)))
    print("Maximum horizontal distance traveled: {0:.2f}".format(ProjectileMotion.maximum_traveled_horizontal_distance(u, theta)))
    print("Maximum vertical distance traveled: {0:.2f}\n".format(ProjectileMotion.maximum_traveled_vertical_distance(u, theta)))


experiments = []
_legend = []

noexperiments = int(input("Enter the number of experiments:\n> "))

print(f"For the next {noexperiments} lines, enter both initial velocity and the degree, separated by a space.")

for i in range(noexperiments):
    print("\n> ", end='')
    u, theta = map(float, input().split()) 
    _legend.append(f"{u} m/s at {theta} degree")
    experiments.append((u, theta))

# Plot the trajectories for different initial velocities
for i in range(len(experiments)):
    y_x_value = ProjectileMotion.get_Dx_Dy_(experiments[i][0], radians(experiments[i][1]))  # Get x and y values using the method
    print(f"{i+1}-Experiment report:")
    exexperiment_report(experiments[i][0], experiments[i][1])
    plot(y_x_value[0], y_x_value[1])  # Plot the trajectory

# Add a legend to the plot
legend(_legend)

# Display the plot
show()
