import requests
import matplotlib.pyplot as plt

# Input the city name from the user
city = input("Enter your city\n> ")

# Get latitude and longitude information for the city
cityinfo = requests.get(f"https://nominatim.openstreetmap.org/search?format=json&q={city}").json()
lat, lon = cityinfo[0]["lat"], cityinfo[0]["lon"]

# Get weather forecast data for the specified location
citytempinfo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m").json()

# Set up the plot
plt.title(f"{city} weather forecast")
plt.xlabel("time")
plt.ylabel("temp")
plt.axis(ymin=min(citytempinfo["hourly"]["temperature_2m"]), ymax=max(citytempinfo["hourly"]["temperature_2m"]), xmin=0, xmax=24)

# Create a list of days and x values for plotting
days, x = [], range(1, 25)

# Iterate through each day's data
y = [citytempinfo["hourly"]["temperature_2m"][0]]
for i in range(1, len(citytempinfo["hourly"]["temperature_2m"])):
    y.append(citytempinfo["hourly"]["temperature_2m"][i])
    
    # Check if 24 data points have been collected (one day's worth)
    if len(y) == 24:
        # Plot the temperature data for the day
        plt.plot(x, y, marker='o')
        
        # Extract the day from the timestamp and add to the list of days
        days.append(citytempinfo["hourly"]["time"][i - 1].split('T')[0])
        
        # Reset the y list for the next day
        y = []

# Add legend showing the days
plt.legend(days)

# Display the plot
plt.show()
