"""
#1: Using Venn Diagrams to Visualize Relationships Between Sets

For your challenge, imagine you’ve created an online questionnaire
asking your classmates the following question: Do you play football, another
sport, or no sports? Once you have the results, create a CSV file, sports.csv.

Write a program to create a Venn diagram to depict the summarized results
of the survey.
"""

from matplotlib_venn import venn2
from sympy import FiniteSet
import matplotlib.pyplot as plt
from random import randint
import pandas

def draw_venn_diagram(sets: list, labels: list[str]):
    """
    Draws a Venn diagram using the matplotlib-venn library.

    Args:
        sets (list): A list of FiniteSet objects to represent the sets in the Venn diagram.
        labels (list of str): A list of labels to describe the sets.

    Returns:
        None: Displays the Venn diagram using Matplotlib.
    """
    venn2(sets, labels)
    plt.show()

def generate_dummy_binary_data(headers: list, size: int, file_name: str):
    """
    Generates dummy binary data and saves it to a CSV file.

    Args:
        headers (list): A list of header labels for the CSV file.
        size (int): The number of data rows to generate.
        file_name (str): The name of the output CSV file.

    Returns:
        None: Saves the generated data to the specified CSV file.
    """
    output = open(file_name, '+a')
    output.write(",".join(headers) + "\n")
    for i in range(size):
        output.write("{0},{1}\n".format(randint(0, 1), randint(0, 1)))
    output.close()

# Commented out because the dummy data file has already been created.
# generate_dummy_binary_data(["Football", "Other Sport"], 20, "dummy_data.csv")

data = pandas.read_csv("dummy_data.csv")

football_players = []
others = []

for i in range(20):
    if data["Football"][i] == 0:
        if data["other sport"][i] == 1:
            others.append(i)
    else:
        football_players.append(i)
        if data["other sport"][i] == 1:
            others.append(i)

draw_venn_diagram([FiniteSet(*football_players), FiniteSet(*others)], ["Football", "Other Sport"])
