import matplotlib.pyplot as plt

# Get the number of categories from the user
nocategories = int(input("Enter the number of categories:\n> "))

# Prompt the user to enter category and expenditure pairs
print(f"\nFor the next {2 * nocategories} lines, enter the category and its expenditure.")

# Create a list to store categories and expenditures
expenditures = [[], []]

# Loop to input category and expenditure data
for i in range(nocategories):
    
    # Read user input for category and expenditure
    cat = input("\nCategory:\n> ")
    expenditure = float(input("Expenditure:\n> "))
    
    # Append category to the first list and expenditure to the second list
    expenditures[0].append(cat)
    expenditures[1].append(expenditure)


# Create a horizontal bar chart using Matplotlib
plt.barh(range(1, nocategories + 1), expenditures[1], height=0.7, align="center")

# Set y-axis tick labels to match the categories
plt.yticks(range(1, nocategories + 1), labels=expenditures[0])

# Adding grid lines to the plot
plt.grid()

# Saving the plot
plt.savefig("weekly expenditures.png")

# Display the plot
plt.show()


