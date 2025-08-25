import requests
import pandas as pd
import config
import db_utils

def extract_data():
    """Fetch weather data from Open-Meteo API."""
    response = requests.get(config.API_URL)
    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")
    return response.json()

def transform_data(data):
    """Transform raw API response into structured dataframe."""
    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    humidity = data["hourly"]["relative_humidity_2m"]

    df = pd.DataFrame({
        "timestamp": times,
        "temperature": temps,
        "humidity": humidity
    })

    return df

def load_data(df):
    print("Loading data into database...")
    conn = db_utils.create_connection(config.DB_PATH)
    db_utils.create_table(conn)

    df.to_sql("weather", conn, if_exists="append", index=False)
    conn.close()


def run_pipeline():
    """Run ETL pipeline end-to-end."""
    print("Extracting data...")
    raw_data = extract_data()

    print("Transforming data...")
    df = transform_data(raw_data)

    print("Loading data into database...")
    load_data(df)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()


