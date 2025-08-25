# Weather Data Pipeline

A simple **ETL (Extract, Transform, Load) pipeline** that fetches hourly weather data from [Open-Meteo API](https://open-meteo.com/en/docs), stores it in a SQLite database, and provides visualizations for temperature and humidity trends.

---

## 🌐 Features

- Fetches hourly weather data (temperature, humidity) for a chosen location.
- Transforms raw JSON data into a structured format.
- Stores data in **SQLite** database (`weather_data.db`).
- Provides **visualizations** of temperature and humidity trends using **matplotlib**.
- Fully modular and extendable for additional weather variables (e.g., wind, rain).

---

## ⚙️ Tech Stack

- **Python 3.9+**
- `requests` – to fetch API data
- `pandas` – for data manipulation
- `matplotlib` – for visualization
- `sqlite3` – database storage

Optional: Jupyter Notebook (`notebooks/weather_analysis.ipynb`) for data exploration.

---

## 🗂️ Repo Structure

weather-data-pipeline/
│── pipeline.py # Main ETL script
│── db_utils.py # Database helper functions
│── config.py # Config & API details
│── visualize_weather.py # Plot temperature/humidity trends
│── requirements.txt # Python dependencies
│── README.md # Project overview
│── weather_data.db # Generated SQLite database
│── notebooks/ # Jupyter notebook for analysis


---

## 🚀 Installation

1. Clone the repo:

```bash
git clone https://github.com/TharunVeluri03/weather-data-pipeline.git
cd weather-data-pipeline

2. (Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt


## 🏃 Running the Pipeline

python pipeline.py

## 📊 Visualizing the Data

python visualize_weather.py

- Generates a line chart for temperature and humidity trends.
- Optional: view data in Jupyter Notebook:





