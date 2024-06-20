import pandas as pd

# Load the dataset
df = pd.read_csv('iot.csv')

# Convert the timestamp column to datetime format
df['ts'] = pd.to_datetime(df['ts'], unit='s')  # Assuming ts is in Unix timestamp format

# Set 'ts' as the index
df.set_index('ts', inplace=True)

# Resample by day and aggregate values to get daily statistics
# Here, we're computing the mean for all numeric columns
daily_summary = df.resample('D').agg({
    'device': 'first',  # Taking the first value for unique identifiers
    'co': 'mean',  # Mean calculation for CO
    'humidity': 'mean',  # Mean calculation for humidity
    'light': 'mean',  # Mean calculation for light
    'lpg': 'mean',  # Mean calculation for LPG
    'motion': 'first',  # Taking the first value for boolean column motion
    'smoke': 'first',  # Taking the first value for boolean column smoke
    'temp': 'mean'  # Mean calculation for temperature
})

# Reset index for cleaner visualization or export to CSV
daily_summary.reset_index(inplace=True)

# Display the first few rows of the summarized dataframe
print(daily_summary.head())

# Optionally, save the daily summary to a CSV file
daily_summary.to_csv('daily_summary.csv', index=False)
