import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have specific start and end times (adjust as needed)
start_time = "2019-06-06 08:00:00"
end_time = "2019-06-15 08:00:00"

# Read the CSV file (adjust filename and column indices)
csv_filename = r"C:\Users\RMCGINT\OneDrive - Wessex Water\Python\WASTE_E24864.csv"
df = pd.read_csv(csv_filename, header=None)

# Assign column names
df.columns = ["signal", "time", "level"]

# Convert time column to datetime format
df["time"] = pd.to_datetime(df["time"])

# Filter the DataFrame to include only data within the specified time range
df_filtered = df[(df["time"] >= start_time) & (df["time"] <= end_time)].copy()

# Set a threshold for level values (adjust as needed)
threshold = 60
# Create a boolean mask for level values exceeding the threshold
above_threshold = df_filtered["level"] > threshold

# Create a boolean mask for level values dropping below the threshold
below_threshold = df_filtered["level"] <= threshold

# Combine the masks to find transitions
transitions = above_threshold != above_threshold.shift()

# Filter transitions where level goes from above to below threshold
drops = transitions & ~above_threshold

# Filter transitions where level goes from below to above threshold
rises = transitions & above_threshold

# Add 24 hours (1 day) to the time for each drop and rise
df_filtered.loc[:, "time_plus_24h"] = df_filtered["time"] + pd.Timedelta(days=1)

# Plot the filtered data
plt.figure(figsize=(10, 6))
plt.plot(df_filtered["time"], df_filtered["level"], label="Level")

plt.axhline(threshold, color="gray", linestyle="--", label="Threshold")
plt.xlabel("Time")
plt.ylabel("Level")
plt.title("Time Series Data with Threshold Transitions (Filtered)")
plt.legend()
plt.grid(True)
plt.show()


# Count the number of individual spills
num_spills = rises.sum()

print(f'Number of individual spills within the given timeframe: {num_spills}')
