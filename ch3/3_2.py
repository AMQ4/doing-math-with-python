from collections import Counter

def mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.
    
    Args:
        numbers (list): List of numeric values.
    
    Returns:
        float: The mean value.
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    Calculate the median of a list of numbers.
    
    Args:
        numbers (list): List of numeric values.
    
    Returns:
        float: The median value.
    """
    numbers = sorted(numbers)
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[middle_index]
    else:
        return mean([numbers[middle_index - 1], numbers[middle_index]])

def mode(numbers):
    """
    Calculate the mode (most common value) of a list of numbers.
    
    Args:
        numbers (list): List of numeric values.
    
    Returns:
        list: List containing tuple(s) with mode(s) and their frequency.
    """
    counter = Counter(numbers)
    return counter.most_common(1)

def variance(numbers):
    """
    Calculate the variance of a list of numbers.
    
    Args:
        numbers (list): List of numeric values.
    
    Returns:
        float: The variance value.
    """
    m = mean(numbers)
    s = 0
    for num in numbers:
        s += (num - m) ** 2
    return s / len(numbers)

def standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers (list): List of numeric values.
    
    Returns:
        float: The standard deviation value.
    """
    return variance(numbers) ** 0.5

def report(numbers):
    """
    Generate a report summarizing mean, median, mode, variance, and standard deviation.
    
    Args:
        numbers (list): List of numeric values.
    """
    print("Data Summary:")
    print(f"Numbers: {numbers}")
    print(f"Mean: {mean(numbers)}")
    print(f"Median: {median(numbers)}")
    print(f"Mode: {mode(numbers)}")
    print(f"Variance: {variance(numbers)}")
    print(f"Standard Deviation: {standard_deviation(numbers)}")

# Read data from file
with open("datafile.txt", "r") as file_numbers:
    numbers = [float(number) for number in file_numbers]

# Call the report function to generate and print the summary
