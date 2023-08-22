import matplotlib.pyplot as plt

# Initialize the first two Fibonacci numbers
fibs = [1, 1]

# Generate the Fibonacci sequence up to the 100th number
for i in range(101):
    fibs.append(fibs[-1] + fibs[-2])

# Calculate and store the ratios of consecutive Fibonacci pairs
ratios_of_consecutive_pairs = []
for i in range(0, 101, 1):
    ratios_of_consecutive_pairs.append(fibs[i + 1] / fibs[i])

# Set labels and title for the plot
plt.ylabel("Ratio")
plt.xlabel("Number")
plt.title("Ratio Between Consecutive Fibonacci Numbers")

# Plot the ratios
plt.plot(ratios_of_consecutive_pairs)

# Display the plot
plt.show()

# Fibonacci number approximation formula: fib(i) = round(phi^i / sqrt(5))
