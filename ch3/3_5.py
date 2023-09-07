import math
import bisect
import pretty_table  # Import the Table class from your pretty_table module

def create_classes(__iterable) -> list:
    """
    Create class intervals for a frequency distribution.

    Args:
        __iterable (iterable): An iterable containing numerical data points.

    Returns:
        list: A list of class intervals represented as pairs (start, end).

    This function calculates class intervals for a frequency distribution
    based on the range of data and the square root rule.
    """
    _min = min(__iterable)
    _max = max(__iterable)
    R = _max - _min
    no_classes = math.ceil(len(__iterable) ** 0.5)
    width = math.ceil(R / no_classes)
    classes = []
    for i in range(1, no_classes + 1):
        classes.append(_min + width * (i - 1))

    return classes

# Open and read data from a file
with open("datafile.txt", 'r') as data:
    numbers = [float(number) for number in data.readlines()]
    
# Sample data for demonstration
numbers = [34, 56, 45, 34, 23, 12, 23, 34, 55, 66, 77, 88, 99, 90, 45, 56, 65, 78, 87, 98, 89, 23, 12, 21, 32, 35, 48]

# Create class intervals for frequency distribution
classes_start = create_classes(numbers)

# Generate class intervals
classes = [[classes_start[i - 1], classes_start[i] - 1] for i in range(1, len(classes_start))]
classes.append((classes_start[len(classes_start) - 1], max(numbers)))

# Initialize a list to store frequencies
freq = [0] * len(classes_start)

# Calculate frequencies for each class interval
for number in numbers:
    index = bisect.bisect_left(classes_start, number)
    if index == len(classes_start) or classes_start[index] > number:
        index -= 1
    freq[index] += 1

# Transpose classes and freq for the table
data_for_table = list(zip(classes, freq))
header = ["Class", "Frequency"]

# Create a frequency distribution table
freq_table = pretty_table.Table(header, data_for_table)
print(freq_table)
