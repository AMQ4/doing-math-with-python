import pandas as pd
import matplotlib.pyplot as plt
import importlib

# Importing the report module
report = importlib.import_module("3_2")

# Read data from the CSV file
data_frame = pd.read_csv("./API_SP.POP.TOTL_DS2_en_csv_v2_5795797.csv")
usa = data_frame[data_frame["Country Code"] == "USA"]
usa_pop_1960_2022 = usa.iloc[0, usa.columns.get_loc("1960"):-1]

# Generate and display the report
report.report(usa_pop_1960_2022)

# Plotting the data
plt.plot(range(1960, 2023), usa_pop_1960_2022)
plt.title("USA Population from 1960 to 2022")
plt.xlabel("Year")
plt.ylabel("Population")
plt.show()
