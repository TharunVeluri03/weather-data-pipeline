# Weather Data Pipeline

A simple **ETL (Extract, Transform, Load) pipeline** that fetches hourly weather data from [Open-Meteo API](https://open-meteo.com/en/docs), stores it in a SQLite database, and provides visualizations for temperature and humidity trends.

---

## 🌐 Features

- Fetches hourly weather data (temperature, humidity) for a chosen location.
- Transforms raw JSON data into a structured format.
- Stores data in **SQLite** database (`weather_data.db` locally, ignored in GitHub).
- Provides **visualizations** of temperature and humidity trends using **matplotlib**.
- Fully modular and extendable for additional weather variables.

---

## ⚙️ Tech Stack

- Python 3.9+
- `requests` – API calls
- `pandas` – data manipulation
- `matplotlib` – visualization
- `sqlite3` – database storage
- Optional: Jupyter Notebook (`notebooks/weather_analysis.ipynb`)

---

## 🚀 Installation

```bash
git clone https://github.com/TharunVeluri03/weather-data-pipeline.git
cd weather-data-pipeline```

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

---

## 🏃 Running the Pipeline

python pipeline.py

- Fetches data from Open-Meteo API.
- Saves structured data in SQLite DB locally (weather_data.db).

---

## 📊 Visualizing the Data

python visualize_weather.py

- Generates a line chart for temperature and humidity trends.
- Optional: view data in Jupyter Notebook:






