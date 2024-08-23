import pandas as pd

data_description = {
    "GHI": "Global Horizontal Irradiance",
    "DNI": "Direct Normal Irradiance",
    "DHI": "Diffuse Horizontal Irradiance",
    "ModA": "Measurements from Module A",
    "ModB": "Measurements from Module B",
    "Tamb": "Ambient Temperature",
    "RH": "Relative Humidity",
    "WS": "Wind Speed",
    "WSgust": "Maximum Wind Gust Speed",
    "WSstdev": "Standard Deviation of Wind Speed",
    "WD": "Wind Direction",
    "WDstdev": "Standard Deviation of Wind Direction",
    "BP": "Barometric Pressure",
    "Cleaning": "Cleaning Status",
    "Precipitation": "Precipitation Rate",
    "TModA": "Temperature of Module A",
    "TModB": "Temperature of Module B"
}

def getStat(df):
    stats = {}
    for column in data_description.keys():
        mean = df[column].mean()
        median = df[column].median()
        std_dev = df[column].std()
        min_val = df[column].min()
        max_val = df[column].max()
        stats[column] = {
            "Mean": f"{mean:.2f}",
            "Median": f"{median:.2f}",
            "Standard deviation": f"{std_dev:.2f}",
            "Min": f"{min_val:.2f}",
            "Max": f"{max_val:.2f}"
        }
    return stats
