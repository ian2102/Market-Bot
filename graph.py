import pandas as pd
import matplotlib.pyplot as plt
import os

data_dir = 'data/'

existing_files = os.listdir(data_dir)

csv_files = [file for file in existing_files if file.endswith('.csv')]

csv_files.sort(key=lambda x: os.path.getmtime(os.path.join(data_dir, x)), reverse=True)

if csv_files:
    newest_file = csv_files[0]
    print("Newest file:", newest_file)
else:
    print("No CSV files found in the data directory.")

df = pd.read_csv(os.path.join(data_dir, newest_file), header=None, names=["Time", "High", "Average", "Low"])

df['Time'] = pd.to_datetime(df['Time'])

plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['High'], label='High')
plt.plot(df['Time'], df['Average'], label='Average')
plt.plot(df['Time'], df['Low'], label='Low')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title(f'Trolls Blood Cost over Time ({df["Time"].iloc[0].strftime("%Y-%m-%d")})')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
