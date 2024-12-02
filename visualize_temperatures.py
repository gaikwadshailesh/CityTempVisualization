import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = "data/temperatures.csv"
data = pd.read_csv(data_path)

# Prepare data
data['Date'] = pd.to_datetime(data['Month'] + " " + data['Year'].astype(str))
data = data.sort_values('Date')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Temperature (°C)'], marker='o', linestyle='-', color='b', label='Temperature')

# Adding title and labels
plt.title("Monthly Average Temperature Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)

# Annotate with max temperature
max_temp = data['Temperature (°C)'].max()
max_date = data.loc[data['Temperature (°C)'].idxmax(), 'Date']
plt.annotate(f'Max: {max_temp}°C', xy=(max_date, max_temp), xytext=(max_date, max_temp+2),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10)

plt.grid(alpha=0.5)
plt.legend()
plt.tight_layout()

# Save and show the plot
plt.savefig("temperature_trends.png", dpi=300)
plt.show()
