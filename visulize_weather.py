import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import config

# Connect to SQLite DB
conn = sqlite3.connect(config.DB_PATH)

# Load last 100 rows (or all) into a DataFrame
df = pd.read_sql_query("SELECT * FROM weather ORDER BY id DESC LIMIT 100", conn)
conn.close()

# Convert timestamp to datetime for plotting
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Plot temperature
plt.figure(figsize=(12,5))
plt.plot(df['timestamp'], df['temperature'], marker='o', color='tomato', label='Temperature (°C)')
plt.plot(df['timestamp'], df['humidity'], marker='x', color='royalblue', label='Humidity (%)')
plt.title("Weather Data Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
