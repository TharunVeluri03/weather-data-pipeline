# Coordinates for London
LAT = 51.51
LON = -0.13

# Variables we want from API
VARIABLES = "temperature_2m,relative_humidity_2m"

# API URL
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&hourly={VARIABLES}"

# Database path
DB_PATH = "weather_data.db"
