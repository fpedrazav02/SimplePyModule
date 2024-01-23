import pandas as pd
from datetime import datetime

def addAirDays(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a new column 'air_days' to the DataFrame indicating the number of days
    the series has been on air. Displays the top 10 records with the most air days.

    Args:
    df (pd.DataFrame): DataFrame containing the series data.

    Returns:
    pd.DataFrame: Updated DataFrame with the 'air_days' column.
    """
    today = pd.to_datetime('today')
    df['first_air_date'] = pd.to_datetime(df['first_air_date'], errors='coerce')
    df['air_days'] = (today - df['first_air_date']).dt.days
    df['air_days'] = df['air_days'].apply(lambda x: 0 if x < 0 else x)
    df['air_days'] = df['air_days'].fillna(0).clip(lower=0)
    print(df.nlargest(2, 'air_days'))
    return df
