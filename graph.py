import pandas as pd
import matplotlib.pyplot as plt
import os

def plot(filepath):

    item_name = "Trolls Blood"
    below_value = 500
    above_value = 550

    data_dir = 'data/'

    existing_files = os.listdir(data_dir)

    csv_files = [file for file in existing_files if file.endswith('.csv')]

    csv_files.sort(key=lambda x: os.path.getmtime(os.path.join(data_dir, x)), reverse=True)

    if csv_files:
        newest_file = csv_files[0]
        print("Newest file:", newest_file)
    else:
        print("No CSV files found in the data directory.")

    df = pd.read_csv(os.path.join(data_dir, newest_file), header=None, names=["Time", "Average", "High", "Low"])

    df['Time'] = pd.to_datetime(df['Time'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['High'], label='High')
    plt.plot(df['Time'], df['Average'], label='Average')
    plt.plot(df['Time'], df['Low'], label='Low')
    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title(f'{item_name} Cost over Time ({df["Time"].iloc[0].strftime("%Y-%m-%d")})')

    plt.axhline(y=below_value, color='red', linestyle='--', label=f'Buy below {below_value}g')
    plt.axhline(y=above_value, color='blue', linestyle='--', label=f'Sell above {above_value}g')

    plt.fill_between(df["Time"], df["Low"], below_value, where=(df["Low"] <= below_value), color='red', alpha=0.3)

    plt.fill_between(df["Time"], df["Low"], above_value, where=(df["Low"] >= above_value), color='blue', alpha=0.3)

    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(filepath)

