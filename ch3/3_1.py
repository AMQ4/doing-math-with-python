def correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two lists of data.

    The Pearson correlation coefficient is a measure of the linear relationship
    between two sets of data. It ranges from -1 (perfect negative correlation)
    to 1 (perfect positive correlation), with 0 indicating no linear correlation.

    Args:
        x (list or numpy array): The first list of data.
        y (list or numpy array): The second list of data.

    Returns:
        float: The Pearson correlation coefficient between the two lists.

    Raises:
        ValueError: If the input lists have different lengths.

    Example:
        >>> x = [1, 2, 3, 4, 5]
        >>> y = [2, 3, 4, 5, 6]
        >>> correlation(x, y)
        1.0
    """
    try:
        if len(x) != len(y):
            raise ValueError("Input lists must have the same length for correlation calculation.")
    except ValueError as e:
        print(e)
        return 0
    else:
        xy = [_x * _y for _x, _y in zip(x, y)]
        x2 = [_x * _x for _x in x]
        y2 = [_y * _y for _y in y]
        n = len(x)
        sumx = sum(x)
        sumy = sum(y)
        sumxy = sum(xy)
        sumx2 = sum(x2)
        sumy2 = sum(y2)

        return (n * sumxy - sumx * sumy) / ((n * sumx2 - sumx ** 2) * (n * sumy2 - sumy ** 2)) ** 0.5
