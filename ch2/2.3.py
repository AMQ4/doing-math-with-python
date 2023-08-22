from matplotlib.pyplot import *
from math import *
import ProjectileMotion


# List of initial velocities

#u_list = [20, 40, 60]
#theta = 45  # Launch angle in degrees
experiments = []
_legend = []

noexperiments = int(input("Enter the number of experiments :\n> "))

print(f"for the next {noexperiments} lines, enter both, initial velocity and the degree, separated by space.")

for i in range(noexperiments):
    print("\n> ", end='')
    u, theta = map(float, input().split()) 
    _legend.append(f"{u}m/s at {theta}")
    experiments.append((u, theta))

# Plot the trajectories for different initial velocities
for experiment in experiments:
    y_x_value = ProjectileMotion.get_Dx_Dy_(experiment[0], radians(experiment[1]))  # Get x and y values using the method
    plot(y_x_value[0], y_x_value[1])  # Plot the trajectory

# Add a legend to the plot
legend(_legend)

# Display the plot
show()
