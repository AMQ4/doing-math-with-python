import math

with open("datafile.txt") as data:
    numbers = [float(line) for line in data]

def calculate_percentile(data, percentile):
    """
    Calculate the specified percentile value from a list of data.

    This function takes a list of numerical data and calculates the specified percentile
    value (between 0 and 100) using linear interpolation between data points.

    Args:
        data (list): A list of numerical data.
        percentile (float): The desired percentile value to calculate (between 0 and 100).

    Returns:
        float: The calculated percentile value.

    Example:
        >>> data = [1.0, 2.0, 3.0, 4.0, 5.0]
        >>> calculate_percentile(data, 50)
        3.0

    Note:
        This function assumes that 'data' is a list of numerical values and 'percentile' is
        a float between 0 and 100. It uses linear interpolation to estimate the percentile
        value between data points.
    """

    sorted_data = sorted(data)
    n = len(sorted_data)
    rank = (percentile / 100) * (n - 1) + 1

    if rank.is_integer():
        return sorted_data[int(rank) - 1]
    else:
        floor_rank = math.floor(rank)
        ceil_rank = math.ceil(rank)
        fractional_part = rank % 1
        percentile_value = (1 - fractional_part) * sorted_data[floor_rank - 1] + fractional_part * sorted_data[ceil_rank - 1]
        return percentile_value

percentile_value = float(input("Enter the desired percentile (0 to 100): "))
result = calculate_percentile(numbers, percentile_value)

print(f"The {percentile_value}th percentile is: {result}")
